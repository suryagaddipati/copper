#!/usr/bin/env python3
"""
Copper Parser Command Line Interface

A command-line tool for parsing and validating Copper files.
"""

import argparse
import sys
import json
from pathlib import Path

# Add parser to path
sys.path.insert(0, str(Path(__file__).parent / "parser"))

try:
    from copper_parser import parse_file, parse_string, ast_to_dict, pretty_print_ast, CopperParserCLI
    from parser import ParseError
except ImportError as e:
    print(f"Error importing parser modules: {e}")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Parse and validate Copper files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s validate examples/orders.copper
  %(prog)s parse examples/orders.copper --format pretty
  %(prog)s parse examples/orders.copper --format json
  %(prog)s validate examples/*.copper
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Parse command
    parse_parser = subparsers.add_parser('parse', help='Parse a Copper file and output AST')
    parse_parser.add_argument('file', help='Copper file to parse')
    parse_parser.add_argument('--format', choices=['pretty', 'json'], default='pretty',
                             help='Output format (default: pretty)')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate one or more Copper files')
    validate_parser.add_argument('files', nargs='+', help='Copper files to validate')
    validate_parser.add_argument('--quiet', '-q', action='store_true',
                                help='Only show errors')
    
    # Check command (alias for validate)
    check_parser = subparsers.add_parser('check', help='Check Copper files (alias for validate)')
    check_parser.add_argument('files', nargs='+', help='Copper files to check')
    check_parser.add_argument('--quiet', '-q', action='store_true',
                             help='Only show errors')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    if args.command == 'parse':
        return handle_parse(args)
    elif args.command in ['validate', 'check']:
        return handle_validate(args)
    
    return 0


def handle_parse(args):
    """Handle the parse command"""
    try:
        result = parse_file(args.file)
        
        if not result.success:
            print(f"Parse error: {result.error}", file=sys.stderr)
            return 1
        
        if args.format == 'json':
            ast_dict = ast_to_dict(result.ast)
            print(json.dumps(ast_dict, indent=2))
        else:  # pretty
            print(pretty_print_ast(result.ast))
        
        return 0
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def handle_validate(args):
    """Handle the validate/check command"""
    success_count = 0
    error_count = 0
    
    # Expand glob patterns if any
    files = []
    for pattern in args.files:
        if '*' in pattern or '?' in pattern:
            # Simple glob expansion
            path = Path(pattern)
            if path.parent.exists():
                matches = list(path.parent.glob(path.name))
                files.extend(matches)
            else:
                print(f"Warning: No files match pattern '{pattern}'", file=sys.stderr)
        else:
            files.append(Path(pattern))
    
    if not files:
        print("No files to validate", file=sys.stderr)
        return 1
    
    for file_path in files:
        if not file_path.exists():
            print(f"✗ {file_path}: File not found")
            error_count += 1
            continue
        
        if not file_path.suffix.lower() == '.copper':
            print(f"✗ {file_path}: Not a .copper file")
            error_count += 1
            continue
        
        result = parse_file(file_path)
        
        if result.success:
            success_count += 1
            if not args.quiet:
                print(f"✓ {file_path}")
                
                # Show summary information
                models = sum(1 for stmt in result.ast.statements 
                           if stmt.__class__.__name__ == 'Model')
                views = sum(1 for stmt in result.ast.statements 
                          if stmt.__class__.__name__ == 'View')
                
                details = []
                if models > 0:
                    details.append(f"{models} model{'s' if models != 1 else ''}")
                if views > 0:
                    details.append(f"{views} view{'s' if views != 1 else ''}")
                
                if details and not args.quiet:
                    print(f"  ({', '.join(details)})")
        else:
            error_count += 1
            print(f"✗ {file_path}")
            print(f"  Error: {result.error}")
    
    # Summary
    total = success_count + error_count
    if not args.quiet:
        print()
        print(f"Validated {total} file{'s' if total != 1 else ''}: "
              f"{success_count} passed, {error_count} failed")
    
    return 0 if error_count == 0 else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\\nInterrupted", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)