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

# This project demonstrates how to design and deploy a highly available web application using AWS networking, compute, database, security, and monitoring services.

# 

# The application follows a \*\*3-tier architecture\*\*:

# 

# \- \*\*Presentation Layer\*\* — Application Load Balancer

# \- \*\*Application Layer\*\* — Flask application running on two EC2 instances

# \- \*\*Database Layer\*\* — Private Amazon RDS MySQL database

# 

# The two application servers are deployed across separate Availability Zones to provide redundancy and failover capability.

# 

# \---

# 

# \## 🏗️ Architecture

# 

# \### AWS 3-Tier Architecture Diagram

# 

# \*\*\[📐 Open Architecture Diagram](architecture/architecture-diagram.png)\*\*

# 

# !\[AWS 3-Tier Architecture](architecture/architecture-diagram.png)

# 

# \### Architecture Flow

# 

# ```text

# &#x20;                        Internet

# &#x20;                           |

# &#x20;                           v

# &#x20;               Application Load Balancer

# &#x20;                           |

# &#x20;                +----------+----------+

# &#x20;                |                     |

# &#x20;                v                     v

# &#x20;         EC2 App Server 1      EC2 App Server 2

# &#x20;         us-east-1a             us-east-1b

# &#x20;                |                     |

# &#x20;                +----------+----------+

# &#x20;                           |

# &#x20;                           v

# &#x20;                   Amazon RDS MySQL

# &#x20;                    Private Subnets

