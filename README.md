## To create Google API Key (JSON-file) you need:
### 1) Register on [Google Cloud](https://cloud.google.com/artifact-registry)
### 2) Create [new project](https://console.cloud.google.com/projectcreate?previousPage=%2Fapis%2Flibrary%3Fproject%3Dconcise-ion-399020&organizationId=0) (use existing project if you want)
### 3) Go to project's [manage](https://console.cloud.google.com/apis/library) and select your new project
![Снимок экрана от 2023-09-26 22-41-50.png](..%2F..%2F..%2FPictures%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BA%D0%B8%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202023-09-26%2022-41-50.png)
### 4) Open Navigation Menu and choose "IAM & Admin" -> "Service accounts"
### 5) Create service account (you can use existing service account if you want) 
### 6) Choose in list your service account and go to "Actions" -> "Manage keys"
### 7) Add key (Create new key) and download JSON-file with API-key

<br><hr>

## Link Google API key:
### After when you have Google API key you should:
### 1) Rename your JSON to "service_account_access.json"
### 2) Move it to "/full/path/to/project/data/service_account_access.json"
### 3) Open "/full/path/to/project/data/constants.py"
### 4) Set "SERVICE_ACCOUNT_FILE" to "/full/path/to/project/data/service_account_access.json"
### 5) Add "SCOPES" (recommend: "https://www.googleapis.com/auth/drive")
### 6) Run this code to get all files on your Google Drive:
```python
from google.oauth2 import service_account
from googleapiclient.discovery import build

# registrate your service acc to use in Python
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/full/path/to/project/data/service_account_access.json'
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

# get all files on your Google Drive (change pageSize, if you need see more/less files)
results = service.files().list(
    pageSize=10,
    fields="nextPageToken, files(id, name, mimeType)"
).execute()
print(results)
```
### 7) Choose from getting files list just that you have in "root" dir on your Google Drive
### 8) Add it to "ROOT_CONTENT" by schema:
```python
ROOT_CONTENT = [
    (
        'dir',  # or 'file'
        'name',  # name your file/dir
        'long_id'  # id of your file/dir
    ),
    # ...
]
```
### 9) Alright!

## Supported commands:
### 1)  ! "sys command"
### 2)  ls
### 3)  pwd
### 4)  cd "path"
### 5)  mkdir "name"
### 6)  rename ./"old_name" ./"new_name"
### 7)  put "file name"
### -)  put -r "dir name"
### 8)  get "file name"
### -)  get -r "dir name"
### 9)  r
### 10) "command 1" && "command 2"
### 11) help
### 12) rm (just for files created by service account)

### -  13) переименовывать файл (при put), если файл с таким именем уже есть
### -  14) drive history
