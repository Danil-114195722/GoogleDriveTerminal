from googleapiclient.http import MediaFileUpload

from data.constants import SERVICE
from work_with_state.id_cur_dir_writter import get_cur_dir_id
from work_with_state.dir_content_writter import get_list_content, set_cur_dir_content


def upload_file(file_name: str, path: str) -> str:
    # id родительской директории
    parent_dir_id = get_cur_dir_id()
    # контент текущей директории
    cur_content = get_list_content()

    # запрет загружать файлы в корень
    if not parent_dir_id:
        return 'ERROR: cannot make dir in "root"'

    file_metadata = {
        'name': file_name,
        'parents': [parent_dir_id]
    }
    media = MediaFileUpload(path, resumable=True)
    new_file = SERVICE.files().create(body=file_metadata, media_body=media, fields='id').execute()

    # обновляем список содержимого текущей папки
    cur_content.append(['file', file_name, new_file.get("id")])
    set_cur_dir_content(content=cur_content)
    print(f'Uploading "{file_name}"\nSuccessfully')
    return f'OK: file "{file_name}" was uploaded'
