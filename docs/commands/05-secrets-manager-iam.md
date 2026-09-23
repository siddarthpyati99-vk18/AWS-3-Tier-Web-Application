# Secrets Manager and IAM

Secret name:

```text
three-tier-db-credentials
```

EC2 IAM role:

```text
3Tier-EC2-SSM-Role
```

Example policy pattern:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["secretsmanager:GetSecretValue"],
      "Resource": "arn:aws:secretsmanager:us-east-1:YOUR_ACCOUNT_ID:secret:three-tier-db-credentials-*"
    }
  ]
}
```

Verification:

```bash
grep -n "secretsmanager" app.py
sudo grep -n "DB_PASSWORD" /etc/systemd/system/three-tier-app.service
```
