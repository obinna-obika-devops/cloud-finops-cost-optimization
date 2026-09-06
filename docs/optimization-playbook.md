# Optimization playbook

1. Validate allocation before optimization.
2. Identify idle resources using utilization and spend thresholds.
3. Review rightsizing candidates against CPU/memory/network and application SLOs.
4. Evaluate Savings Plans/reserved capacity only after usage is stable.
5. Check storage lifecycle, unattached volumes, snapshots, and data-transfer patterns.
6. For Kubernetes, compare requested vs observed resources and track workload cost.
7. Quantify expected savings, risk, owner, and rollback before execution.
8. Re-measure unit economics after the change.
