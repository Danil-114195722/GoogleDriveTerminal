from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build


SCOPES = ['your_scope']
SERVICE_ACCOUNT_FILE = 'full/path/to/data/service_account_access.json'

CREDENTIALS = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SERVICE = build('drive', 'v3', credentials=CREDENTIALS)

ROOT_CONTENT = [
    ('dir', 'name', 'long_id'),
    ('dir', 'name', 'long_id'),
    ('dir', 'name', 'long_id'),
    ('dir', 'name', 'long_id'),
]

BASE_DIR = Path(__file__).parent.parent
