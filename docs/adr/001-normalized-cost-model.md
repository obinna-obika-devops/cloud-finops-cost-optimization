# ADR 001: Normalize cost data before policy evaluation

## Decision
Use a normalized tabular cost model between provider billing exports and optimization policies.

## Why
Provider billing schemas change and contain many dimensions. Policy code should consume stable fields such as date, account, team, environment, service, cost center, and cost.

## Consequences
The ingestion layer can evolve independently from analytics and policy logic. Real AWS CUR/Athena ingestion can be added later without rewriting the FinOps controls.
