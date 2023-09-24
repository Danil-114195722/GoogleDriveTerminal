import io
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

from data.constants import SERVICE
from work_with_state.dir_content_writter import get_list_content


def download_file(file_name: str) -> str:
    try:
        # все файлы и папки в текущем каталоге
        cur_content = get_list_content()

        # юзер ввёл неверный файл
        if file_name not in map(lambda sublist: sublist[1], cur_content):
            return 'ERROR: such file not found!'
        elif list(filter(lambda sublist: sublist[1] == file_name, cur_content))[0][0] == 'dir':
            return 'ERROR: cannot upload dir!'
        else:
            # ID файла, который нужно скачать
            file_id = list(filter(lambda sublist: sublist[1] == file_name, cur_content))[0][-1]

        request = SERVICE.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)

        print('Download:')
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f'\r{int(status.progress() * 100)}%', end='')

        # загрузка байт в локальный файл
        with open(file_name, 'wb') as local_file:
            local_file.write(file.getvalue())
            print(f'\nFile "{file_name}" have been uploaded successfully')
        return f'OK: file "{file_name}" was uploaded'

    except HttpError as error:
        return f'ERROR: you got this error: {error}'
