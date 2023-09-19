from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
import io

from pyenv import dirs_in_root


# $$$_IMPORTANT_START_$$$
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/service_account_access.json'
# $$$_IMPORTANT_END_$$$

# $$$_IMPORTANT_START_$$$
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)
# $$$_IMPORTANT_END_$$$


# ID папки, из которой вы хотите получить файлы
folder_id = '156JGMFm4bJ599pDROIf8TUDgTwhVo71G'
# Строка запроса для получения файлов из определенной папки
query = f"'{folder_id}' in parents"


# query = f"'root' in parents and mimeType = 'application/vnd.google-apps.folder'"


# results = service.files().list(q=query, spaces='drive', fields='nextPageToken, files(id, name)', pageToken=None).execute()
# results = service.files().list(q=query, fields='nextPageToken, files(id, name, mimeType)', pageToken=None).execute()

root = service.files().list(pageSize=dirs_in_root, fields="files(id, name, mimeType)").execute()

print(results)
for res in results.get('files'):
    print(res)
