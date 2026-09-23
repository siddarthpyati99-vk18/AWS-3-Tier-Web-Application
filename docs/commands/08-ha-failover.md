# High Availability Failover

Normal:

```text
EC2 #1 -> Healthy
EC2 #2 -> Healthy
```

Failover:

```text
EC2 #1 -> Unhealthy
EC2 #2 -> Healthy
ALB    -> Application still accessible
```

Evidence:
- Target Group screenshot showing one unhealthy and one healthy target.
- ALB DNS screenshot showing the application still working.
