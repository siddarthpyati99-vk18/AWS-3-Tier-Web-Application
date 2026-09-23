\## 🏗️ Architecture



\### AWS 3-Tier Architecture Diagram



\[!\[AWS 3-Tier Architecture](architecture/architecture-diagram.png)](architecture/architecture-diagram.png)

\### Architecture Flow



```text

Internet

\&#x20;  |

\&#x20;  v

Application Load Balancer

\&#x20;  |

\&#x20;  +----> EC2 App Server 1

\&#x20;  |

\&#x20;  +----> EC2 App Server 2

\&#x20;             |

\&#x20;             v

\&#x20;      Amazon RDS MySQL


