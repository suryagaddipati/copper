#!/usr/bin/env python3
"""
Manual HTTP server for Copper parser (no FastAPI required)
Simple HTTP server that serves the parser API endpoints
"""

import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import glob
from antlr_parser import validate_copper_syntax


class CopperAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, content_type='application/json'):
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_GET(self):
        path = self.path.split('?')[0]
        
        if path == '/':
            self._set_headers()
            response = {
                "message": "Copper Parser API (Manual Server)",
                "version": "1.0.0",
                "endpoints": {
                    "/parse": "Parse Copper content (POST)",
                    "/examples": "Get example Copper files",
                    "/health": "Health check"
                }
            }
            self.wfile.write(json.dumps(response, indent=2).encode())
            
        elif path == '/health':
            self._set_headers()
            response = {"status": "healthy", "service": "copper-parser-api-manual"}
            self.wfile.write(json.dumps(response).encode())
            
        elif path == '/examples':
            self._set_headers()
            examples = self._get_examples()
            self.wfile.write(json.dumps(examples, indent=2).encode())
            
        elif path.startswith('/examples/'):
            example_name = urllib.parse.unquote(path[10:])  # Remove '/examples/'
            self._set_headers()
            example = self._get_example(example_name)
            if example:
                self.wfile.write(json.dumps(example, indent=2).encode())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(json.dumps({"error": f"Example '{example_name}' not found"}).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    def do_POST(self):
        if self.path == '/parse':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            try:
                request_data = json.loads(post_data)
                content = request_data.get('code', request_data.get('content', ''))
                
                result = validate_copper_syntax(content)
                
                # Convert parsed nodes to serializable format
                models = []
                for model in result["models"]:
                    models.append({
                        "name": model.name,
                        "type": model.type.value,
                        "line_number": model.line_number,
                        "properties": model.properties,
                        "children": [
                            {
                                "name": child.name,
                                "type": child.type.value,
                                "line_number": child.line_number,
                                "properties": child.properties
                            }
                            for child in model.children
                        ]
                    })
                
                views = []
                for view in result["views"]:
                    views.append({
                        "name": view.name,
                        "type": view.type.value,
                        "line_number": view.line_number,
                        "properties": view.properties,
                        "children": [
                            {
                                "name": child.name,
                                "type": child.type.value,
                                "line_number": child.line_number,
                                "properties": child.properties
                            }
                            for child in view.children
                        ]
                    })
                
                response = {
                    "valid": result["valid"],
                    "errors": result["errors"],
                    "warnings": result["warnings"],
                    "statistics": result["statistics"],
                    "models": models,
                    "views": views
                }
                
                self._set_headers()
                self.wfile.write(json.dumps(response, indent=2).encode())
                
            except Exception as e:
                self.send_response(500)
                self._set_headers()
                error_response = {"error": f"Parse error: {str(e)}"}
                self.wfile.write(json.dumps(error_response).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def _get_examples(self):
        examples = []
        examples_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "examples")
        
        if not os.path.exists(examples_dir):
            return examples
        
        copper_files = glob.glob(os.path.join(examples_dir, "*.copper"))
        
        for file_path in copper_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                filename = os.path.basename(file_path)
                name = filename.replace('.copper', '').replace('_', ' ').title()
                
                # Extract description from first comment if available
                description = f"Example Copper file: {name}"
                lines = content.split('\n')
                for line in lines[:5]:  # Check first 5 lines for description
                    if line.strip().startswith('#') and len(line.strip()) > 2:
                        description = line.strip()[1:].strip()
                        break
                
                examples.append({
                    "name": name,
                    "content": content,
                    "description": description
                })
            
            except Exception:
                # Skip files that can't be read
                continue
        
        return examples

    def _get_example(self, example_name):
        examples_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "examples")
        
        # Convert display name back to filename
        filename = example_name.lower().replace(' ', '_') + '.copper'
        file_path = os.path.join(examples_dir, filename)
        
        if not os.path.exists(file_path):
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract description
            description = f"Example Copper file: {example_name}"
            lines = content.split('\n')
            for line in lines[:5]:
                if line.strip().startswith('#') and len(line.strip()) > 2:
                    description = line.strip()[1:].strip()
                    break
            
            return {
                "name": example_name,
                "content": content,
                "description": description
            }
        
        except Exception:
            return None

    def log_message(self, format, *args):
        # Suppress default logging, we'll do our own
        print(f"{self.address_string()} - {format % args}")


def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CopperAPIHandler)
    print(f"🔥 Copper Parser API running on http://localhost:{port}")
    print("   Press Ctrl+C to stop")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        httpd.server_close()


if __name__ == '__main__':
    run_server()