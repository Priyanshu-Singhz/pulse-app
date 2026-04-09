import boto3
from botocore.exceptions import ClientError

ses = boto3.client("ses", region_name="us-east-1")
SENDER = "noreply@pulse-app.com"

def send_verification_email(to_email: str, token: str):
    link = f"https://pulse-app.com/verify?token={token}"
    try:
        ses.send_email(
            Source=SENDER,
            Destination={"ToAddresses": [to_email]},
            Message={
                "Subject": {"Data": "Verify your Pulse account"},
                "Body": {"Html": {"Data": f"<a href='{link}'>Verify Email</a>"}},
            },
        )
    except ClientError as e:
        raise RuntimeError(f"Email send failed: {e}")
