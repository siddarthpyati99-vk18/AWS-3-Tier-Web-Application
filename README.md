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









