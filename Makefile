default: test

.ONESHELL:

.PHONY: lint-python
lint-python: ## Lint python scripts
	black --diff --check --exclude='ve/|venv/' .

.PHONY: pytest
pytest: ## Run python tests
	pytest -sv --color=yes ./test/runner.py
