# FinOps governance

## Allocation
Every chargeable workload should map to an owner, team, application, environment, and cost center. Untagged spend is surfaced rather than silently assigned.

## Showback vs chargeback
- **Showback:** report costs to teams without financial transfer; best for early adoption.
- **Chargeback:** allocate costs to budgets/business units; use when ownership and allocation quality are mature.

## Unit economics
Prefer business-aligned metrics such as cost/request, cost/transaction, cost/customer, and cost/workload-hour. Track both total spend and efficiency so optimization does not simply reduce capacity.

## Governance cadence
- Daily: anomaly signals and pipeline policy checks
- Weekly: engineering optimization review
- Monthly: budget/forecast review and allocation reconciliation
- Quarterly: rate/architecture review and commitment strategy

## Guardrail
Automated deletion or resizing should require explicit approval and a rollback path for material production changes.
