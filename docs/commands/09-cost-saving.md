# Cost Saving

After screenshots and testing:

- Stop both EC2 instances.
- Stop RDS when supported and not in use.
- Delete the NAT Gateway if the environment is paused for an extended period.
- Delete the ALB if the environment is no longer needed.

Keep reusable VPC architecture and configuration if you plan to rebuild the project.
Check AWS Billing/Cost Management for actual charges.
