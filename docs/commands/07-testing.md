# Testing and Troubleshooting

```bash
curl http://localhost:5000
sudo systemctl status three-tier-app
sudo systemctl restart three-tier-app
sudo journalctl -u three-tier-app --no-pager -n 50
cd /home/ssm-user/three-tier-app
ls -la
source venv/bin/activate
pip list
```

Expected:

```text
AWS 3-Tier Web Application
Application + RDS Connected
Siddarth
Shrusti
```
