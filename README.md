# Cloud FinOps Cost Optimization Platform

A production-oriented FinOps reference implementation for turning cloud billing data into engineering decisions: allocation, budgets, forecasting, anomaly detection, rightsizing, and policy automation.

> **Reviewing this for a role?** Start with the [5-minute recruiter/interview walkthrough](docs/recruiter-walkthrough.md) for a fast path through the cloud cost engineering evidence.

## What this demonstrates
- AWS Cost & Usage Report-style ingestion using **synthetic demo data**
- Cost by team, account, environment, service, and cost center
- Showback/chargeback and unit economics
- Budget and tagging policy gates
- Trend forecasting and spend anomaly detection
- Rightsizing and idle-resource opportunity detection
- Kubernetes cost allocation concepts
- AWS Budgets and Cost Anomaly Detection Terraform examples
- Scheduled Markdown/CSV reporting
- CI quality gates with Python tests, Terraform validation, Checkov, and FinOps policy checks

## Architecture
`Billing/CUR -> normalized cost model -> analytics -> policies -> reports -> engineering action`

The repository intentionally contains no real billing credentials or claimed production savings. Sample billing data is synthetic.

## Recruiter evidence path

- [Recruiter / Interview Walkthrough](docs/recruiter-walkthrough.md)
- ingestion and analytics code — cost normalization, forecasting and anomaly logic
- policy checks — budget, tagging and governance controls
- Terraform examples — cloud-native budget/anomaly controls
- tests + `.github/` — CI and validation evidence
- sample reports — how data becomes engineering action

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python -m finops.cli analyze data/sample/cost_usage.csv --output reports/demo-report.md
python -m finops.cli forecast data/sample/cost_usage.csv --days 30
python -m finops.cli anomalies data/sample/cost_usage.csv
python scripts/finops_gate.py
```

## Recruiter signal
This project complements infrastructure, platform, SRE, and DevSecOps work by showing that I can operate cloud systems with an understanding of **economics, accountability, and efficiency**.

## Production extension
Connect the normalized ingestion layer to AWS CUR/Athena, OpenCost/Kubernetes telemetry, AWS Organizations billing dimensions, and an approved reporting destination. Apply human approval to material optimization actions before automation.

## Scope

This is a portfolio/reference implementation using synthetic demo billing data. It does not claim real production savings or access to live customer billing information.
