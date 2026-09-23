# \# AWS 3-Tier Highly Available Web Application

# 

# A production-style \*\*3-tier web application deployed on AWS\*\*, designed with high availability, private networking, secure database access, IAM-based authentication, secrets management, and monitoring.

# 

# The application uses \*\*Amazon VPC, Application Load Balancer, Amazon EC2, Flask, Gunicorn, Amazon RDS for MySQL, AWS Secrets Manager, IAM, and Amazon CloudWatch\*\*.

# 

# \---

# 

# \## 🚀 Project Overview

# 

# This project demonstrates how to design and deploy a highly available web application using AWS networking and compute services.

# 

# The application follows a \*\*3-tier architecture\*\*:

# 

# \- \*\*Presentation Layer\*\* — Application Load Balancer

# \- \*\*Application Layer\*\* — Flask application running on two EC2 instances

# \- \*\*Database Layer\*\* — Private Amazon RDS MySQL database

# 

# The two application servers are deployed across separate Availability Zones to improve availability and provide failover capability.

# 

# \---

# 

# \## 🏗️ Architecture

# 

# !\[AWS 3-Tier Architecture](architecture/architecture-diagram.png)







\## 📸 Project Screenshots



\### 1. VPC Configuration



!\[VPC Configuration](screenshots/01-vpc.png)



\---



\### 2. Subnet Configuration



!\[Subnet Configuration](screenshots/02-subnets.png)



\---



\### 3. Route Tables



!\[Route Tables](screenshots/03-route-tables.png)



\---



\### 4. Application Load Balancer Security Group



!\[ALB Security Group](screenshots/04a-alb-security-group.png)



\---



\### 5. EC2 Security Group



!\[EC2 Security Group](screenshots/04b-ec2-security-group.png)



\---



\### 6. RDS Security Group



!\[RDS Security Group](screenshots/04c-rds-security-group.png)



\---



\### 7. EC2 Application Servers



!\[EC2 Instances](screenshots/05-ec2.png)



\---



\### 8. Application Load Balancer



!\[Application Load Balancer](screenshots/06-alb.png)



\---



\### 9. Target Group Health



!\[Target Group](screenshots/07-target-group.png)



\---



\### 10. Amazon RDS MySQL



!\[RDS MySQL](screenshots/08-rds.png)



\---



\### 11. AWS Secrets Manager



!\[Secrets Manager](screenshots/09-secrets-manager.png)



\---



\### 12. Amazon CloudWatch



!\[CloudWatch Monitoring](screenshots/10-cloudwatch.png)



\---



\### 13. Running Application



!\[Running Application](screenshots/11-application.png)



\---



\### 14. High Availability Failover Test



!\[High Availability Failover](screenshots/12-ha-failover.png)

