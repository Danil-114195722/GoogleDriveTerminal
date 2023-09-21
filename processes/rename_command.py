from data.constants import SERVICE
from work_with_state.current_dir_writter import set_cur_dir, get_cur_dir
from work_with_state.dir_content_writter import set_cur_dir_content, get_list_content
from work_with_state.recent_dir_id_writter import set_id_recent_dirs, get_id_recent_dir
from work_with_state.id_cur_dir_writter import set_cur_dir_id


# переименование файла или папки
def rename_file(old_name: str, new_name: str):
    # все файлы и папки в текущем каталоге
    cur_content = get_list_content()

    # юзер ввёл неверную директорию
    if old_name not in map(lambda sublist: sublist[1], cur_content):
        return 'ERROR: such dir or file not found!'
    else:
        # строка контента переименовываемого объекта
        elem_line = list(filter(lambda sublist: sublist[1] == old_name, cur_content))[0]
        # id файла или папки, которую нужно переименовать
        elem_id = elem_line[-1]

    # добавляем расширение старого названия к новому, если оно не было указано в новом
    if '.' not in new_name:
        new_name += '.' + old_name.split('.')[-1]

    # Выполнение запроса на обновление метаданных для переименования объекта
    SERVICE.files().update(fileId=elem_id, body={'name': new_name}).execute()

    # обновление контента текущего каталога
    cur_content[cur_content.index(elem_line)][1] = new_name
    set_cur_dir_content(content=cur_content)

    return f'OK: rename "{old_name}" to "{new_name}"'
