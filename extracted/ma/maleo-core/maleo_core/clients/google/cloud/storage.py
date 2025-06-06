import os
from datetime import timedelta
from google.auth import default
from google.cloud.storage import Bucket, Client
from google.oauth2 import service_account
from typing import Optional

class GoogleCloudStorage:
    _client:Optional[Client] = None
    _bucket:Optional[Bucket] = None

    @classmethod
    def initialize(cls) -> None:
        """Initialize the cloud storage if not already initialized."""
        if cls._client is None:
            #* Setup credentials with fallback chain
            credentials = None
            credentials_file = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
            try:
                if credentials_file:
                    credentials = service_account.Credentials.from_service_account_file(credentials_file)
                else:
                    credentials, _ = default()
            except Exception as e:
                raise ValueError(f"Failed to initialize credentials: {str(e)}")

            cls._client = Client(credentials=credentials)

            #* Preload bucket
            bucket_name = os.getenv("GCS_BUCKET_NAME")
            if not bucket_name:
                cls._client.close()
                raise ValueError("GCS_BUCKET_NAME environment variable must be set")

            #* Validate bucket existence
            bucket = cls._client.lookup_bucket(bucket_name)
            if bucket is None:
                raise ValueError(f"Bucket '{bucket_name}' does not exist.")

            cls._bucket = bucket

    @classmethod
    def dispose(cls) -> None:
        """Dispose of the cloud storage and release any resources."""
        if cls._client is not None:
            cls._client.close()
            cls._client = None
            cls._bucket = None

    @classmethod
    def _get_client(cls) -> Client:
        """Retrieve the cloud storage client, initializing it if necessary."""
        cls.initialize()
        return cls._client

    @classmethod
    def generate_signed_url(cls, location:str) -> str:
        """
        generate signed URL of a file in the bucket based on its location.

        Args:
            location: str
                Location of the file inside the bucket

        Returns:
            str: File's pre-signed download url

        Raises:
            ValueError: If the file does not exist
        """
        cls.initialize()
        blob = cls._bucket.blob(blob_name=location)
        if not blob.exists():
            raise ValueError(f"File '{location}' did not exists.")

        url = blob.generate_signed_url(version="v4", expiration=timedelta(minutes=15), method="GET")
        return url