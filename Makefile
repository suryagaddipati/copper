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
STUDIO_DIR := studio
GENERATED_DIR := studio/src/lib/parser/generated
GRAMMAR_FILE := $(GRAMMAR_DIR)/Copper.g4

# Port configuration with defaults (can be overridden)
STUDIO_PORT ?= 3000
STUDIO_PORT_EXTRA1 ?= 3001
STUDIO_PORT_EXTRA2 ?= 3002
PORTS := $(STUDIO_PORT) $(STUDIO_PORT_EXTRA1) $(STUDIO_PORT_EXTRA2)

# Help target - shows available commands
help:
	@echo "$(BLUE)🚀 Copper Development Environment$(NC)"
	@echo "=================================="
	@echo ""
	@echo "$(GREEN)Available targets:$(NC)"
	@echo "  $(YELLOW)make all$(NC)        - Build and start unified Next.js application"
	@echo "  $(YELLOW)make build$(NC)      - Build everything (parser + dependencies)"
	@echo "  $(YELLOW)make parser$(NC)     - Generate ANTLR parser from grammar"
	@echo "  $(YELLOW)make start$(NC)      - Start unified development server"
	@echo "  $(YELLOW)make dev$(NC)        - Start unified development server"
	@echo "  $(YELLOW)make stop$(NC)       - Stop all running servers"
	@echo "  $(YELLOW)make kill-ports$(NC) - Force kill processes on development ports"
	@echo "  $(YELLOW)make install$(NC)    - Install all dependencies"
	@echo "  $(YELLOW)make clean$(NC)      - Clean generated files"
	@echo "  $(YELLOW)make test$(NC)       - Quick parser smoke test"
	@echo "  $(YELLOW)make help$(NC)       - Show this help message"
	@echo ""
	@echo "$(GREEN)Quick start:$(NC)"
	@echo "  $(BLUE)make$(NC)            - Build and start everything"
	@echo "  $(BLUE)make dev$(NC)        - Start unified Next.js application"
	@echo ""
	@echo "$(GREEN)Port configuration:$(NC)"
	@echo "  Default port: $(STUDIO_PORT) (Next.js will use next available if taken)"
	@echo "  Custom port:  $(YELLOW)STUDIO_PORT=3001 make dev$(NC)"

# Build everything
build: parser install
	@echo "$(GREEN)✅ Build complete!$(NC)"

# Generate ANTLR parser from grammar
parser: $(GENERATED_DIR)/CopperLexer.js

$(GENERATED_DIR)/CopperLexer.js: $(GRAMMAR_FILE)
	@echo "$(BLUE)🔨 Generating ANTLR JavaScript parser...$(NC)"
	@if [ ! -f "$(GRAMMAR_FILE)" ]; then \
		echo "$(RED)❌ Grammar file not found: $(GRAMMAR_FILE)$(NC)"; \
		exit 1; \
	fi
	@mkdir -p $(GENERATED_DIR)
	@antlr4 -Dlanguage=JavaScript -o $(GENERATED_DIR) $(GRAMMAR_FILE)
	@if [ -f "$(GENERATED_DIR)/CopperParser.js" ]; then \
		echo "$(GREEN)✅ JavaScript parser generated successfully$(NC)"; \
		echo "   Files: CopperLexer.js, CopperParser.js, CopperListener.js"; \
	else \
		echo "$(RED)❌ Parser generation failed$(NC)"; \
		exit 1; \
	fi

# Install dependencies
install:
	@echo "$(BLUE)📦 Installing Next.js dependencies...$(NC)"
	@if [ ! -d "$(STUDIO_DIR)/node_modules" ]; then \
		cd $(STUDIO_DIR) && npm install; \
		echo "$(GREEN)✅ Next.js dependencies installed$(NC)"; \
	else \
		echo "$(YELLOW)⏭️  Next.js dependencies already installed$(NC)"; \
	fi

# Start development environment
start: dev

dev: build
	@echo "$(BLUE)🚀 Starting Copper Studio (unified Next.js application)...$(NC)"
	@echo "$(YELLOW)🛑 Stopping any existing servers and clearing ports...$(NC)"
	@echo "$(YELLOW)🔌 Killing processes on ports $(PORTS)...$(NC)"
	@lsof -ti:$(STUDIO_PORT) | xargs kill -9 2>/dev/null || true
	@lsof -ti:$(STUDIO_PORT_EXTRA1) | xargs kill -9 2>/dev/null || true
	@lsof -ti:$(STUDIO_PORT_EXTRA2) | xargs kill -9 2>/dev/null || true
	@echo "$(YELLOW)🔌 Killing Next.js processes...$(NC)"
	@ps aux | grep -E "node.*next.*dev|next-server" | grep -v grep | awk '{print $$2}' | xargs kill -9 2>/dev/null || true
	@echo "$(YELLOW)⏳ Waiting for processes to clear...$(NC)"
	@sleep 3
	@echo "$(BLUE)🚀 Starting unified Next.js development server...$(NC)"
	@cd $(STUDIO_DIR) && PORT=$(STUDIO_PORT) npm run dev &
	@sleep 3
	@echo ""
	@echo "$(GREEN)🎉 Copper Studio ready!$(NC)"
	@echo "========================================"
	@echo "$(BLUE)🌐 Application: http://localhost:$(STUDIO_PORT)$(NC)"
	@echo "$(BLUE)🔌 API Routes:  http://localhost:$(STUDIO_PORT)/api$(NC)"
	@echo ""
	@echo "$(YELLOW)Press Ctrl+C to stop, or run 'make stop'$(NC)"

# Stop all servers
stop:
	@echo "$(YELLOW)🛑 Stopping all servers and clearing ports...$(NC)"
	@echo "$(YELLOW)🔌 Killing Next.js processes...$(NC)"
	@pkill -f "node.*next.*dev" 2>/dev/null || true
	@pkill -f "next-server" 2>/dev/null || true
	@echo "$(YELLOW)🔌 Killing processes on ports $(PORTS)...$(NC)"
	@lsof -ti:$(STUDIO_PORT) | xargs kill -9 2>/dev/null || true
	@lsof -ti:$(STUDIO_PORT_EXTRA1) | xargs kill -9 2>/dev/null || true
	@lsof -ti:$(STUDIO_PORT_EXTRA2) | xargs kill -9 2>/dev/null || true
	@echo "$(GREEN)✅ All servers stopped and ports cleared$(NC)"

# Kill processes on development ports only
kill-ports:
	@echo "$(YELLOW)🔌 Forcefully killing processes on development ports...$(NC)"
	@pkill -f "node.*next.*dev" 2>/dev/null || true
	@pkill -f "next-server" 2>/dev/null || true
	@lsof -ti:$(STUDIO_PORT) | xargs kill -9 2>/dev/null || true
	@lsof -ti:$(STUDIO_PORT_EXTRA1) | xargs kill -9 2>/dev/null || true
	@lsof -ti:$(STUDIO_PORT_EXTRA2) | xargs kill -9 2>/dev/null || true
	@echo "$(GREEN)✅ Development ports cleared$(NC)"

# Test parser functionality (quick smoke test)
test:
	@echo "$(BLUE)🧪 Testing Next.js application...$(NC)"
	@cd $(STUDIO_DIR) && npm run build && echo "$(GREEN)✅ Build test passed!$(NC)" || echo "$(RED)❌ Build test failed$(NC)"

# Clean generated files
clean:
	@echo "$(YELLOW)🧹 Cleaning generated files...$(NC)"
	@rm -rf $(GENERATED_DIR)
	@cd $(STUDIO_DIR) && rm -rf .next node_modules/.cache 2>/dev/null || true
	@echo "$(GREEN)✅ Generated files cleaned$(NC)"

# Check requirements
check:
	@echo "$(BLUE)🔍 Checking requirements...$(NC)"
	@command -v antlr4 >/dev/null 2>&1 || { echo "$(RED)❌ antlr4 command not found$(NC)"; exit 1; }
	@command -v node >/dev/null 2>&1 || { echo "$(RED)❌ node not found$(NC)"; exit 1; }
	@command -v npm >/dev/null 2>&1 || { echo "$(RED)❌ npm not found$(NC)"; exit 1; }
	@echo "$(GREEN)✅ All requirements satisfied$(NC)"