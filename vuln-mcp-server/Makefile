.PHONY: health test install run clean help

# JSON-RPC message templates
INIT_MSG = {"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test-client","version":"1.0.0"}}}
INITIALIZED_MSG = {"jsonrpc":"2.0","method":"notifications/initialized","params":{}}
TOOLS_LIST_MSG = {"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}
RESOURCES_LIST_MSG = {"jsonrpc":"2.0","id":3,"method":"resources/list","params":{}}

help:
	@echo "Available commands:"
	@echo "  install      - Install dependencies with uv"
	@echo "  health       - Run health check for MCP server"
	@echo "  test         - Run pytest tests"
	@echo "  run          - Run MCP server with custom RPC (use RPC='...' make run)"
	@echo "  clean        - Clean up temporary files"

install:
	uv sync

health:
	@echo "Running MCP server health check..."
	@echo "1. Testing initialization..."
	@echo '$(INIT_MSG)' | uv run main.py 2>/dev/null | grep -q '"result"' && echo "✅ Initialization: OK" || echo "❌ Initialization: FAILED"
	@echo "2. Testing tools/list..."
	@(echo '$(INIT_MSG)'; echo '$(INITIALIZED_MSG)'; echo '$(TOOLS_LIST_MSG)') | uv run main.py 2>/dev/null | grep -q '"tools"' && echo "✅ Tools: OK" || echo "❌ Tools: FAILED"
	@echo "3. Testing resources/list..."
	@(echo '$(INIT_MSG)'; echo '$(INITIALIZED_MSG)'; echo '$(RESOURCES_LIST_MSG)') | uv run main.py 2>/dev/null | grep -q '"resources"' && echo "✅ Resources: OK" || echo "❌ Resources: FAILED"
	@echo "Health check completed."

test:
	pytest

run:
ifdef RPC
	@echo "Sending custom RPC: $(RPC)"
	@(echo '$(INIT_MSG)'; echo '$(INITIALIZED_MSG)'; echo '$(RPC)') | uv run main.py
else
	uv run main.py
endif

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf *.pyc
