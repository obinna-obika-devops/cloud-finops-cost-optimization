SHELL := /bin/bash
.PHONY: test analyze forecast anomalies gate

test:
	python -m pytest -q
analyze:
	python -m finops.cli analyze data/sample/cost_usage.csv --output reports/demo-report.md
forecast:
	python -c "from finops.analytics import load,forecast; print(f'30d forecast: $${forecast(load(\"data/sample/cost_usage.csv\")):,.2f}')"
anomalies:
	python -c "from finops.analytics import load,anomalies; print(anomalies(load(\"data/sample/cost_usage.csv\")))"
gate:
	python scripts/finops_gate.py
