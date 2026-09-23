# Gunicorn and systemd

```bash
cd /home/ssm-user/three-tier-app
source venv/bin/activate
gunicorn --workers 2 --bind 0.0.0.0:5000 app:app
```

Systemd service:

```ini
[Unit]
Description=Three Tier Flask Application
After=network.target

[Service]
User=ssm-user
Group=ssm-user
WorkingDirectory=/home/ssm-user/three-tier-app
Environment="PATH=/home/ssm-user/three-tier-app/venv/bin"
ExecStart=/home/ssm-user/three-tier-app/venv/bin/gunicorn --workers 2 --bind 0.0.0.0:5000 app:app
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl restart three-tier-app
sudo systemctl enable three-tier-app
sudo systemctl status three-tier-app
sudo journalctl -u three-tier-app --no-pager -n 50
```
