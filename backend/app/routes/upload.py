from fastapi import APIRouter, Depends
import boto3
from pydantic import BaseModel

router = APIRouter()
s3 = boto3.client("s3")
BUCKET = "pulse-app-media"

class PresignRequest(BaseModel):
    filename: str
    content_type: str

@router.post("/upload/presign")
def get_presigned_url(body: PresignRequest):
    key = f"uploads/{body.filename}"
    url = s3.generate_presigned_url(
        "put_object",
        Params={"Bucket": BUCKET, "Key": key, "ContentType": body.content_type},
        ExpiresIn=300,
    )
    return {"url": url, "key": key}
