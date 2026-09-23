# AWS 3-Tier Highly Available Web Application

A production-style **3-tier web application deployed on AWS**, designed with high availability, private networking, secure database access, IAM-based authentication, secrets management, monitoring, and multi-AZ failover.

The application uses **Amazon VPC, Application Load Balancer, Amazon EC2, Flask, Gunicorn, Amazon RDS for MySQL, AWS Secrets Manager, IAM, AWS Systems Manager, and Amazon CloudWatch**.

---

## 🚀 Project Overview

This project demonstrates how to design, deploy, secure, monitor, and test a highly available web application using AWS cloud infrastructure.

The application follows a **3-tier architecture**:

- **Presentation Layer** — Application Load Balancer
- **Application Layer** — Flask application running on two EC2 instances
- **Database Layer** — Private Amazon RDS MySQL database

The application servers are deployed across two Availability Zones:

- **Availability Zone 1:** `us-east-1a`
- **Availability Zone 2:** `us-east-1b`

This architecture provides redundancy and allows the Application Load Balancer to continue serving requests when one application server becomes unavailable.

### Application Flow

```text
Internet
   |
   v
Application Load Balancer
   |
   +-------------------+
   |                   |
   v                   v
EC2 App Server 1    EC2 App Server 2
us-east-1a          us-east-1b
   |                   |
   +---------+---------+
             |
             v
      Amazon RDS MySQL
```

### Security Flow

```text
Internet
    |
    | HTTP : 80
    v
Application Load Balancer
    |
    | TCP : 5000
    v
EC2 Application Servers
    |
    | MySQL : 3306
    v
Private Amazon RDS MySQL
```

---

## 🏗️ Architecture

### AWS 3-Tier Architecture Diagram

[![AWS 3-Tier Architecture](architecture/architecture-diagram.png)](architecture/architecture-diagram.png)

### Architecture Components

| Layer | AWS Service | Purpose |
|---|---|---|
| Presentation | Application Load Balancer | Public entry point and traffic distribution |
| Application | Amazon EC2 | Runs Flask application |
| Application | Gunicorn | Production WSGI server |
| Database | Amazon RDS MySQL | Private relational database |
| Security | AWS IAM | Role-based AWS access |
| Security | AWS Secrets Manager | Secure database credentials |
| Monitoring | Amazon CloudWatch | Metrics and alarms |
| Management | AWS Systems Manager | Secure EC2 access |

---

## ☁️ AWS Infrastructure

### Amazon VPC

- **VPC:** `3-Tier-WebApp-VPC`
- **CIDR:** `10.0.0.0/16`
- **Region:** `us-east-1`

### Subnets

| Tier | Availability Zone | CIDR |
|---|---|---|
| Public | us-east-1a | 10.0.1.0/24 |
| Public | us-east-1b | 10.0.2.0/24 |
| Application | us-east-1a | 10.0.11.0/24 |
| Application | us-east-1b | 10.0.12.0/24 |
| Database | us-east-1a | 10.0.21.0/24 |
| Database | us-east-1b | 10.0.22.0/24 |

### Internet Gateway

The Internet Gateway provides internet connectivity for the public subnets and allows the Application Load Balancer to receive internet traffic.

### Route Tables

The project uses separate routing for the different tiers:

- Public route table → Internet Gateway
- Private application route table → NAT Gateway
- Private database route table → Local VPC traffic only

### NAT Gateway

The NAT Gateway was used to provide outbound internet connectivity for resources in the private application subnets.

It was removed after testing to reduce AWS costs.

---

## ⚖️ Application Load Balancer

The Application Load Balancer provides the public entry point for the application.

Configuration:

- **Name:** `3Tier-Application-ALB`
- **Scheme:** Internet-facing
- **Listener:** HTTP port `80`
- **Target Group:** `3Tier-App-TG`
- **Target Port:** `5000`

Traffic is distributed between the two EC2 application servers.

```text
Internet
   |
   v
Application Load Balancer
   |
   +----> EC2 App Server 1
   |
   +----> EC2 App Server 2
```

---

## 🖥️ EC2 Application Servers

Two EC2 instances run the Flask application.

### EC2 Server 1

- **Name:** `3Tier-App-Server-1`
- **Availability Zone:** `us-east-1a`
- **Subnet:** Private Application Subnet
- **Application Port:** `5000`

### EC2 Server 2

- **Name:** `3Tier-App-Server-2`
- **Availability Zone:** `us-east-1b`
- **Subnet:** Private Application Subnet
- **Application Port:** `5000`

### Application Stack

```text
Python
   |
Flask
   |
Gunicorn
   |
Amazon EC2
```

---

## 🗄️ Amazon RDS MySQL

The database layer uses a private Amazon RDS MySQL database.

Configuration:

- **Engine:** MySQL
- **Database:** `studentdb`
- **Public Access:** No
- **Port:** `3306`
- **Subnet:** Private Database Subnets
- **Security:** Accessible only from the EC2 security group

The application retrieves student records from the RDS database.

---

## 🔐 Security

Security Groups were configured using tier-based access.

### ALB Security Group

```text
HTTP : 80
Source: 0.0.0.0/0
```

### EC2 Security Group

```text
TCP : 5000
Source: ALB Security Group
```

### RDS Security Group

```text
MySQL : 3306
Source: EC2 Security Group
```

This creates the following controlled traffic path:

```text
Internet
    |
    | HTTP : 80
    v
   ALB
    |
    | TCP : 5000
    v
   EC2
    |
    | MySQL : 3306
    v
   RDS
```

---

## 🔑 AWS Secrets Manager

Database credentials are stored securely in AWS Secrets Manager.

**Secret Name:**

`three-tier-db-credentials`

The Flask application retrieves the database credentials using the IAM role attached to the EC2 instances.

```text
EC2
 |
 | IAM Role
 v
AWS Secrets Manager
 |
 | Database Credentials
 v
Flask Application
 |
 v
Amazon RDS MySQL
```

Database passwords are not stored in the application source code.

---

## 👤 IAM

The EC2 instances use an IAM role:

`3Tier-EC2-SSM-Role`

The role provides the permissions required for:

- AWS Systems Manager access
- AWS Secrets Manager access

This avoids storing AWS access keys directly on the EC2 instances.

---

## 📊 Amazon CloudWatch

CloudWatch monitoring was configured for:

- Application Load Balancer
- EC2 Application Server 1
- EC2 Application Server 2
- Amazon RDS MySQL

Configured alarms include:

- ALB unhealthy targets
- EC2 high CPU utilization
- RDS high CPU utilization

These alarms provide visibility into application and infrastructure health.

---

## 🔄 High Availability Test

A failover test was performed by stopping one EC2 application server.

### Before Failover

```text
EC2 #1 → Healthy
EC2 #2 → Healthy
```

### During Failover

```text
EC2 #1 → Unhealthy
EC2 #2 → Healthy

ALB → Continues serving the application
```

The Application Load Balancer continued routing requests to the healthy application server.

This demonstrated the application's multi-AZ failover design.

---

# 📸 AWS Project Screenshots

## VPC Configuration

[![VPC Configuration](screenshots/01-vpc%20.png)](screenshots/01-vpc%20.png)

## Subnet Configuration

[![Subnet Configuration](screenshots/02-subnets.png)](screenshots/02-subnets.png)

## Route Tables

[![Route Tables](screenshots/03-route-tables.png)](screenshots/03-route-tables.png)

## ALB Security Group

[![ALB Security Group](screenshots/04a-alb-security-group.png)](screenshots/04a-alb-security-group.png)

## EC2 Security Group

[![EC2 Security Group](screenshots/04b-ec2-security-group.png)](screenshots/04b-ec2-security-group.png)

## RDS Security Group

[![RDS Security Group](screenshots/04c-rds-security-group.png)](screenshots/04c-rds-security-group.png)

## EC2 Application Servers

[![EC2 Application Servers](screenshots/05-ec2.png)](screenshots/05-ec2.png)

## Application Load Balancer

[![Application Load Balancer](screenshots/06-alb.png)](screenshots/06-alb.png)

## Target Group

[![Target Group](screenshots/07-target-group.png)](screenshots/07-target-group.png)

## Amazon RDS MySQL

[![Amazon RDS MySQL](screenshots/08-rds.png)](screenshots/08-rds.png)

## AWS Secrets Manager

[![AWS Secrets Manager](screenshots/09-secrets-manager.png)](screenshots/09-secrets-manager.png)

## Amazon CloudWatch

[![Amazon CloudWatch](screenshots/10-cloudwatch.png)](screenshots/10-cloudwatch.png)

## Running Application

[![Running Application](screenshots/11-application.png)](screenshots/11-application.png)

## High Availability Failover

[![High Availability Failover](screenshots/12-ha-failover.png)](screenshots/12-ha-failover.png)

---

## 🧪 Application Testing

The application was tested using:

```bash
curl http://localhost:5000
```

The application successfully:

- Started Flask/Gunicorn
- Retrieved credentials from AWS Secrets Manager
- Connected to Amazon RDS MySQL
- Retrieved student records
- Displayed the application

---

## 🛠️ Technologies Used

### AWS

- Amazon VPC
- Amazon EC2
- Application Load Balancer
- Amazon RDS MySQL
- AWS Secrets Manager
- AWS IAM
- Amazon CloudWatch
- AWS Systems Manager
- Internet Gateway
- NAT Gateway

### Application

- Python
- Flask
- Gunicorn
- PyMySQL
- Boto3

### Development Tools

- Git
- GitHub
- AWS CLI
- AWS Systems Manager

---

## 📂 Repository Structure

```text
AWS-3-Tier-Web-Application/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── architecture/
│   └── architecture-diagram.png
│
├── screenshots/
│   ├── 01-vpc.png
│   ├── 02-subnets.png
│   ├── 03-route-tables.png
│   ├── 04a-alb-security-group.png
│   ├── 04b-ec2-security-group.png
│   ├── 04c-rds-security-group.png
│   ├── 05-ec2.png
│   ├── 06-alb.png
│   ├── 07-target-group.png
│   ├── 08-rds.png
│   ├── 09-secrets-manager.png
│   ├── 10-cloudwatch.png
│   ├── 11-application.png
│   └── 12-ha-failover.png
│
└── docs/
    └── commands/
        ├── 01-aws-cli-and-ssm.md
        ├── 02-ec2-python-setup.md
        ├── 03-flask-application.md
        ├── 04-rds-connectivity.md
        ├── 05-secrets-manager-iam.md
        ├── 06-gunicorn-systemd.md
        ├── 07-testing.md
        ├── 08-ha-failover.md
        └── 09-cost-saving.md
```

---

## 📚 Project Documentation

Detailed implementation commands used to build and test this project are available below.

| # | Documentation | Description |
|---|---|---|
| 01 | [AWS CLI & SSM](docs/commands/01-aws-cli-and-ssm.md) | AWS CLI and EC2 Systems Manager |
| 02 | [EC2 & Python Setup](docs/commands/02-ec2-python-setup.md) | EC2, Python, virtual environment and packages |
| 03 | [Flask Application](docs/commands/03-flask-application.md) | Flask application configuration |
| 04 | [RDS Connectivity](docs/commands/04-rds-connectivity.md) | Amazon RDS MySQL connectivity |
| 05 | [Secrets Manager & IAM](docs/commands/05-secrets-manager-iam.md) | Secure database credentials and IAM |
| 06 | [Gunicorn & systemd](docs/commands/06-gunicorn-systemd.md) | Production application service |
| 07 | [Testing](docs/commands/07-testing.md) | Application and database testing |
| 08 | [HA Failover](docs/commands/08-ha-failover.md) | High availability and failover testing |
| 09 | [Cost Saving](docs/commands/09-cost-saving.md) | AWS resource cost optimization |

---

## 💰 Cost Optimization

After completing testing, unused AWS resources can be stopped or deleted to reduce costs.

Resources considered for cost optimization:

- EC2 instances
- Amazon RDS
- NAT Gateway
- Application Load Balancer
- Elastic IP addresses

The NAT Gateway and Application Load Balancer were removed after testing to reduce ongoing AWS charges.

---

## 🔒 Security Best Practices

Never commit the following to a public GitHub repository:

```text
AWS Access Keys
AWS Secret Keys
Database Passwords
Secrets Manager Secret Values
.pem Private Keys
.env Files Containing Credentials
API Keys
Private SSH Keys
```

Sensitive information should also be removed or redacted from screenshots.

Database credentials in this project are managed through AWS Secrets Manager rather than being hard-coded in the application.

---

## 🎓 Key Learning Outcomes

This project provided hands-on experience with:

- AWS VPC architecture
- Public and private subnets
- Route tables
- Internet Gateway
- NAT Gateway
- Amazon EC2
- Application Load Balancer
- Multi-AZ architecture
- Flask
- Gunicorn
- Amazon RDS MySQL
- IAM roles
- AWS Secrets Manager
- Security Groups
- Amazon CloudWatch
- AWS Systems Manager
- High availability
- Failover testing
- Git and GitHub

---

## 👨‍💻 Author

### Siddarth Pyati

Engineering Student | Cloud Computing Enthusiast

**Areas of Interest**

- Cloud Computing
- Amazon Web Services
- DevOps
- Cloud Infrastructure
- Cloud Security

---

## 📄 License

This project is licensed under the MIT License.
