# AWS 3-Tier Highly Available Web Application

## 🏗️ Architecture

### AWS 3-Tier Architecture Diagram

[![AWS 3-Tier Architecture](architecture/architecture-diagram.png)](architecture/architecture-diagram.png)

### Architecture Flow

```text
Internet
   |
   v
Application Load Balancer
   |
   +----> EC2 App Server 1
   |
   +----> EC2 App Server 2
              |
              v
       Amazon RDS MySQL
