ROOT_CAUSE_RULES = [
    {
        "name": "database/connectivity failure",
        "keywords": ["database", "db", "sql", "connection", "timeout", "deadlock"],
        "recommendation": "Check DB availability, connection pool limits, credentials, schema migrations, and slow queries.",
    },
    {
        "name": "memory pressure or OOM",
        "keywords": ["memory", "oom", "heap", "allocation", "outofmemory"],
        "recommendation": "Inspect memory usage, heap limits, recent deployments, and potential leaks.",
    },
    {
        "name": "network or DNS issue",
        "keywords": ["network", "dns", "socket", "refused", "unreachable", "reset"],
        "recommendation": "Verify DNS, firewall rules, service discovery, network latency, and upstream availability.",
    },
    {
        "name": "authentication or authorization failure",
        "keywords": ["auth", "token", "permission", "unauthorized", "forbidden", "credential"],
        "recommendation": "Check token expiry, IAM permissions, secrets rotation, and service account configuration.",
    },
    {
        "name": "deployment/configuration regression",
        "keywords": ["config", "missing", "invalid", "deploy", "version", "rollback"],
        "recommendation": "Compare recent config/deployment changes and roll back suspicious releases if needed.",
    },
]
