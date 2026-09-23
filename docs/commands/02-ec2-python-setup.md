# EC2 and Python Setup

```bash
sudo dnf update -y
mkdir -p /home/ssm-user/three-tier-app
cd /home/ssm-user/three-tier-app
python3 -m venv venv
source venv/bin/activate
pip install Flask PyMySQL boto3 gunicorn
python3 --version
pip --version
```
