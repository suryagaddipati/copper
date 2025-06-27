# Copper Development Environment Makefile
# A beautiful way to build and run the Copper parser and web application

.PHONY: all build parser clean start dev stop install-web install-api test test-all test-verbose help kill-ports

# Default target
all: build start

# Colors for beautiful output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[1;33m
RED := \033[0;31m
NC := \033[0m # No Color

# Configuration
GRAMMAR_DIR := grammar
API_DIR := studio/api
WEB_DIR := studio/web
GENERATED_DIR := src/parser/generated
GRAMMAR_FILE := $(GRAMMAR_DIR)/Copper.g4

# Help target - shows available commands
help:
	@echo "$(BLUE)🚀 Copper Development Environment$(NC)"
	@echo "=================================="
	@echo ""
	@echo "$(GREEN)Available targets:$(NC)"
	@echo "  $(YELLOW)make all$(NC)        - Build parser and start development environment"
	@echo "  $(YELLOW)make build$(NC)      - Build everything (parser + dependencies)"
	@echo "  $(YELLOW)make parser$(NC)     - Generate ANTLR parser from grammar"
	@echo "  $(YELLOW)make start$(NC)      - Start API and web servers"
	@echo "  $(YELLOW)make dev$(NC)        - Start development environment"
	@echo "  $(YELLOW)make stop$(NC)       - Stop all running servers"
	@echo "  $(YELLOW)make kill-ports$(NC) - Force kill processes on development ports"
	@echo "  $(YELLOW)make install$(NC)    - Install all dependencies"
	@echo "  $(YELLOW)make clean$(NC)      - Clean generated files"
	@echo "  $(YELLOW)make test$(NC)       - Quick parser smoke test"
	@echo "  $(YELLOW)make test-all$(NC)   - Run comprehensive unit tests"
	@echo "  $(YELLOW)make test-verbose$(NC) - Run unit tests with verbose output"
	@echo "  $(YELLOW)make help$(NC)       - Show this help message"
	@echo ""
	@echo "$(GREEN)Quick start:$(NC)"
	@echo "  $(BLUE)make$(NC)            - Build and start everything"
	@echo "  $(BLUE)make dev$(NC)        - Start development servers"

# Build everything
build: parser install
	@echo "$(GREEN)✅ Build complete!$(NC)"

# Generate ANTLR parser from grammar
parser: $(GENERATED_DIR)/CopperLexer.py

$(GENERATED_DIR)/CopperLexer.py: $(GRAMMAR_FILE)
	@echo "$(BLUE)🔨 Generating ANTLR parser...$(NC)"
	@if [ ! -f "$(GRAMMAR_FILE)" ]; then \
		echo "$(RED)❌ Grammar file not found: $(GRAMMAR_FILE)$(NC)"; \
		exit 1; \
	fi
	@mkdir -p $(GENERATED_DIR)
	@cp $(GRAMMAR_FILE) . && \
		antlr4 -Dlanguage=Python3 -o $(GENERATED_DIR) Copper.g4 && \
		rm Copper.g4
	@if [ -f "$(GENERATED_DIR)/CopperParser.py" ]; then \
		echo "$(GREEN)✅ Parser generated successfully$(NC)"; \
		echo "   Files: CopperLexer.py, CopperParser.py, CopperListener.py"; \
	else \
		echo "$(RED)❌ Parser generation failed$(NC)"; \
		exit 1; \
	fi

# Install dependencies
install: install-web install-api

install-web:
	@echo "$(BLUE)📦 Installing web dependencies...$(NC)"
	@if [ ! -d "$(WEB_DIR)/node_modules" ]; then \
		cd $(WEB_DIR) && npm install; \
		echo "$(GREEN)✅ Web dependencies installed$(NC)"; \
	else \
		echo "$(YELLOW)⏭️  Web dependencies already installed$(NC)"; \
	fi

install-api:
	@echo "$(BLUE)📦 Checking API dependencies...$(NC)"
	@if [ ! -f "$(API_DIR)/requirements.txt" ]; then \
		echo "$(RED)❌ API requirements.txt not found$(NC)"; \
		exit 1; \
	fi
	@echo "$(YELLOW)💡 API dependencies listed in $(API_DIR)/requirements.txt$(NC)"
	@echo "   Install with: pip install -r $(API_DIR)/requirements.txt"

# Start development environment
start: dev

dev: build
	@echo "$(BLUE)🚀 Starting Copper development environment...$(NC)"
	@echo "$(YELLOW)🛑 Stopping any existing servers and clearing ports...$(NC)"
	@pkill -f "npm run dev" 2>/dev/null || true
	@pkill -f "main.py" 2>/dev/null || true
	@pkill -f "main.py" 2>/dev/null || true
	@pkill -f "vite" 2>/dev/null || true
	@pkill -f "uvicorn" 2>/dev/null || true
	@pkill -f "fastapi" 2>/dev/null || true
	@echo "$(YELLOW)🔌 Killing processes on ports 3000, 3001, 3002, 8000...$(NC)"
	@lsof -ti:3000 | xargs kill -9 2>/dev/null || true
	@lsof -ti:3001 | xargs kill -9 2>/dev/null || true
	@lsof -ti:3002 | xargs kill -9 2>/dev/null || true
	@lsof -ti:8000 | xargs kill -9 2>/dev/null || true
	@echo "$(YELLOW)⏳ Waiting for ports to clear...$(NC)"
	@sleep 3
	@echo "$(BLUE)🔥 Starting API server with UFC integration on port 8000...$(NC)"
	@cd $(API_DIR) && python3 main.py &
	@sleep 3
	@echo "$(BLUE)🌐 Starting web development server on port 3000...$(NC)"
	@cd $(WEB_DIR) && npm run dev &
	@sleep 2
	@echo ""
	@echo "$(GREEN)🎉 Development environment ready!$(NC)"
	@echo "========================================"
	@echo "$(BLUE)📱 Web App: http://localhost:3000$(NC)"
	@echo "$(BLUE)🔌 API:     http://localhost:8000$(NC)"
	@echo ""
	@echo "$(YELLOW)Press Ctrl+C to stop, or run 'make stop'$(NC)"

# Stop all servers
stop:
	@echo "$(YELLOW)🛑 Stopping all servers and clearing ports...$(NC)"
	@pkill -f "npm run dev" 2>/dev/null || true
	@pkill -f "main.py" 2>/dev/null || true
	@pkill -f "main.py" 2>/dev/null || true
	@pkill -f "vite" 2>/dev/null || true
	@pkill -f "uvicorn" 2>/dev/null || true
	@pkill -f "fastapi" 2>/dev/null || true
	@echo "$(YELLOW)🔌 Killing processes on ports 3000, 3001, 3002, 8000...$(NC)"
	@lsof -ti:3000 | xargs kill -9 2>/dev/null || true
	@lsof -ti:3001 | xargs kill -9 2>/dev/null || true
	@lsof -ti:3002 | xargs kill -9 2>/dev/null || true
	@lsof -ti:8000 | xargs kill -9 2>/dev/null || true
	@echo "$(GREEN)✅ All servers stopped and ports cleared$(NC)"

# Kill processes on development ports only
kill-ports:
	@echo "$(YELLOW)🔌 Forcefully killing processes on development ports...$(NC)"
	@lsof -ti:3000 | xargs kill -9 2>/dev/null || true
	@lsof -ti:3001 | xargs kill -9 2>/dev/null || true
	@lsof -ti:3002 | xargs kill -9 2>/dev/null || true
	@lsof -ti:8000 | xargs kill -9 2>/dev/null || true
	@echo "$(GREEN)✅ Development ports cleared$(NC)"

# Test parser functionality (quick smoke test)
test: parser
	@echo "$(BLUE)🧪 Testing parser functionality...$(NC)"
	@python3 -c "from src.parser.antlr_parser import validate_copper_syntax; result = validate_copper_syntax('dimension: test_id { expression: \$${table.id} }'); print('$(GREEN)✅ Parser test passed!$(NC)' if result['valid'] else '$(RED)❌ Parser test failed$(NC)'); print('Dimensions:', result['statistics']['total_dimensions']); print('Errors:', result['errors'] if result['errors'] else 'None')"

# Run comprehensive unit tests
test-all: parser
	@echo "$(BLUE)🧪 Running comprehensive unit tests...$(NC)"
	@PYTHONPATH=src python3 -m unittest discover tests/parser/ -s tests/parser/ -p "test_*.py"
	@echo "$(GREEN)✅ All tests completed!$(NC)"

# Run unit tests with verbose output
test-verbose: parser
	@echo "$(BLUE)🧪 Running unit tests with verbose output...$(NC)"
	@PYTHONPATH=src python3 -m unittest discover tests/parser/ -v
	@echo "$(GREEN)✅ Verbose tests completed!$(NC)"

# Clean generated files
clean:
	@echo "$(YELLOW)🧹 Cleaning generated files...$(NC)"
	@rm -rf $(GENERATED_DIR)
	@echo "$(GREEN)✅ Generated files cleaned$(NC)"

# Development shortcuts
web-dev:
	@cd $(WEB_DIR) && npm run dev

api-dev:
	@cd $(API_DIR) && python3 main.py

# Check requirements
check:
	@echo "$(BLUE)🔍 Checking requirements...$(NC)"
	@command -v antlr4 >/dev/null 2>&1 || { echo "$(RED)❌ antlr4 command not found$(NC)"; exit 1; }
	@command -v python3 >/dev/null 2>&1 || { echo "$(RED)❌ python3 not found$(NC)"; exit 1; }
	@command -v node >/dev/null 2>&1 || { echo "$(RED)❌ node not found$(NC)"; exit 1; }
	@command -v npm >/dev/null 2>&1 || { echo "$(RED)❌ npm not found$(NC)"; exit 1; }
	@echo "$(GREEN)✅ All requirements satisfied$(NC)"