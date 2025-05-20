# mlops

12 Factors:

1. Codebase - Git
Why: A single codebase tracked in revision control, many deploys.
2. Dependencies - Docker/poetry/uv
Why: Explicitly declare and isolate dependencies.
3. Config - Environment
Why: Store config in the environment.
4. Backing services - Databases, etc
Why: Treat backing services as attached resources.
5. Build, release, run
Why: Strictly separate build and run stages.
6. Processes
Why: Execute the app as one or more stateless processes.
7. Port binding
Why: Export services via port binding.
8. Concurrency
Why: Scale out via the process model.
9. Disposability
Why: Maximize robustness with fast startup and graceful shutdown.
10. Dev/prod parity
Why: Keep development, staging, and production as similar as possible.
11. Logs
Why: Treat logs as event streams.
12. Admin processes
Why: Run admin/management tasks as one-off processes.