# Kubernetes cost allocation

Workloads should expose cost dimensions through labels/annotations:

- `finops.team`
- `finops.cost-center`
- `finops.environment`
- `finops.application`
- `finops.owner`

A production implementation can join Kubernetes resource requests/usage with node and cloud-provider pricing through OpenCost. This repository keeps the integration provider-neutral and uses synthetic examples.
