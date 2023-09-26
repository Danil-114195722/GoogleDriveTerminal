from data.constants import SERVICE
from work_with_state.dir_content_writter import set_cur_dir_content, get_list_content
from work_with_state.id_cur_dir_writter import get_cur_dir_id


# удаление файла (если он создан сервисным аккаунтом)
def remove_service_file(file_name: str) -> str:
    # id родительской папки
    parent_dir_id = get_cur_dir_id()
    # все файлы и папки в текущем каталоге
    cur_content = get_list_content()

    # запрет создавать папку в корне
    if not parent_dir_id:
        return 'ERROR: cannot make dir in "root"'

    file_id_to_delete = 'your_file_id_here'

    # Выполнение запроса на удаление файла
    SERVICE.files().delete(fileId=file_id_to_delete).execute()

    print(f'File with ID {file_id_to_delete} has been deleted.')
    # обновляем список содержимого текущей папки
    # cur_content.remove(['dir', new_dir_name, new_dir.get("id")])
    set_cur_dir_content(content=cur_content)
    return f'OK: rm {file_name}'
