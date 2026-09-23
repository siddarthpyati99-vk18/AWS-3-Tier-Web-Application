# AWS 3-Tier Web Application

Highly available AWS 3-tier web application using Amazon VPC, Application Load Balancer, EC2, Flask, Amazon RDS MySQL, AWS Secrets Manager, IAM and Amazon CloudWatch.

## Architecture

```text
Internet
   |
Application Load Balancer
   |-------------------|
   v                   v
EC2 App #1          EC2 App #2
AZ1                 AZ2
   |-------------------|
            |
         RDS MySQL
        Private DB

EC2 IAM Role --> Secrets Manager
CloudWatch --> ALB / EC2 / RDS
```

## Application Flow

1. Browser connects to the ALB DNS name.
2. ALB routes traffic to a healthy EC2 server.
3. Flask/Gunicorn runs on port 5000.
4. Flask retrieves database credentials from Secrets Manager using the EC2 IAM role.
5. Flask connects to private RDS MySQL.
6. Student records are displayed.
7. CloudWatch monitors ALB, EC2 and RDS.

## AWS Components

- VPC: `3-Tier-WebApp-VPC`
- CIDR: `10.0.0.0/16`
- Two Availability Zones
- Public, private application and private database subnets
- Internet Gateway
- NAT Gateway during active testing
- Application Load Balancer
- Two EC2 application servers
- Flask + Gunicorn
- Amazon RDS MySQL
- AWS Secrets Manager
- IAM
- Amazon CloudWatch

## High Availability Test

EC2 application server #1 was intentionally stopped. The ALB detected it as unhealthy and continued serving the application through EC2 #2.

```text
EC2 #1 -> Unhealthy
EC2 #2 -> Healthy
ALB    -> Application still accessible
```

## Command Documentation

See `docs/commands/` for the implementation commands:

1. AWS CLI and SSM
2. EC2 and Python setup
3. Flask application
4. RDS connectivity
5. Secrets Manager and IAM
6. Gunicorn and systemd
7. Testing and troubleshooting
8. HA failover
9. Cost saving

## Security

Never commit AWS access keys, database passwords, Secrets Manager secret values, PEM files, `.env` files or credential files.

Use placeholders such as:

```text
YOUR_ACCOUNT_ID
YOUR_INSTANCE_ID
YOUR_RDS_ENDPOINT
YOUR_ALB_DNS
```

## Author

**Siddarth Pyati**
