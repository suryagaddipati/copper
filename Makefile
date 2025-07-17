# Copper Build System

.PHONY: clean build test parser install dev-install sync

# Python environment
PYTHON := uv run python
ANTLR_JAR := antlr-4.13.2-complete.jar
ANTLR_URL := https://www.antlr.org/download/$(ANTLR_JAR)

# Directories
GRAMMAR_DIR := grammar
PARSER_DIR := copper/parser/generated
SRC_DIR := src

# Sync dependencies from lock file
sync:
	uv sync

# Install development dependencies
dev-install:
	uv sync --dev

# Install package
install:
	uv sync

# Download ANTLR if not present
$(ANTLR_JAR):
	wget $(ANTLR_URL)

# Generate parser from ANTLR grammar
parser: $(ANTLR_JAR)
	mkdir -p $(PARSER_DIR)
	java -jar $(ANTLR_JAR) -Dlanguage=Python3 -visitor -no-listener \
		-o $(PARSER_DIR) $(GRAMMAR_DIR)/Copper.g4
	touch $(PARSER_DIR)/__init__.py

# Clean generated files
clean:
	rm -rf $(PARSER_DIR)
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Build package
build: parser
	$(PYTHON) setup.py build

# Run tests
test: dev-install
	$(PYTHON) -m pytest tests/ -v --cov=$(SRC_DIR)

# Format code
format: dev-install
	$(PYTHON) -m black $(SRC_DIR) tests/

# Type checking
typecheck: dev-install
	$(PYTHON) -m mypy $(SRC_DIR)

# Lint code
lint: format typecheck

# Full development setup
setup: dev-install parser

# Run example
example:
	$(PYTHON) examples/basic_demo.py

# UFC examples
ufc-explore:
	cd examples/ufc && $(PYTHON) explore.py