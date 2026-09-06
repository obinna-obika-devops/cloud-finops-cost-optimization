# Recruiter / Interview Walkthrough

This page highlights the cloud cost engineering and FinOps signal in this repository.

## 5-minute review path

1. Read `README.md` for the cost-management architecture and scope.
2. Inspect the ingestion/analysis code for cost normalization and reporting logic.
3. Inspect policy checks for tagging, budget and governance rules.
4. Inspect Terraform examples for cloud-native budget and anomaly controls.
5. Inspect tests and `.github/` for CI validation.
6. Review sample reports and synthetic data to see how engineering decisions are surfaced.

## What this project proves

This project treats cost as an engineering concern rather than a finance-only report. It shows how cloud usage data can become actionable signals for teams through allocation, budgets, forecasting, anomaly detection and rightsizing recommendations.

Key themes:

- normalized cloud cost data
- showback/chargeback concepts
- team and environment allocation
- budget and tagging guardrails
- anomaly detection
- spend forecasting
- rightsizing and idle-resource detection
- Kubernetes cost-allocation concepts
- Terraform-based cost controls
- automated reporting

## Interview discussion points

### Why should DevOps or platform engineers care about FinOps?
Architecture decisions affect both reliability and cost. Platform teams can make good defaults visible and enforceable so product teams understand the financial impact of infrastructure choices.

### How should optimization automation be handled?
Recommendations should be evidence-based and risk-aware. Low-risk reporting can be automated aggressively, while material changes such as downsizing production resources should require validation and approval.

### How would this work with real billing data?
The normalized model could ingest AWS CUR/Athena outputs, organization/account dimensions and Kubernetes/OpenCost telemetry. Reports could then feed dashboards, chat notifications or engineering scorecards.

### What would productionization add?
A production implementation would add real billing connectors, durable storage, access controls, scheduled pipelines, historical baselines, owner mapping, exception workflows and business-approved cost KPIs.

## Validation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python -m finops.cli analyze data/sample/cost_usage.csv --output reports/demo-report.md
python scripts/finops_gate.py
```

## Scope and integrity

This is a portfolio/reference implementation using synthetic demo billing data. It does not claim real production savings or access to live customer billing information.
