# Rightsizing runbook

**Trigger:** sustained low utilization or unexpected cost growth.

1. Confirm ownership and workload criticality.
2. Compare 7/14/30-day utilization against requests and limits.
3. Check SLOs, latency, queue depth, and peak behavior.
4. Estimate monthly savings and operational risk.
5. Propose a smaller instance/resource request in staging first.
6. Validate performance and error budgets.
7. Apply with a rollback plan and monitor for at least one business cycle.
8. Record realized cost and unit-economics impact.

Never optimize solely on CPU percentage when memory, network, storage I/O, or burst behavior may be the actual constraint.
