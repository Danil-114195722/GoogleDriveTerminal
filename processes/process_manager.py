from os.path import abspath, isfile, exists
from re import sub as re_sub, findall as re_findall

from processes import (cd_command, ls_command, pwd_command,
                       mkdir_command, rename_command,
                       system_interaction, help_command,
                       get_command, put_command)


def process_help(command: str) -> str:
    content = help_command.show_help_manual()
    print(content)

    return f'OK: {command}'


def process_sys(command: str) -> str:
    sys_com = command[1:]
    system_interaction.system_command_exec(command=sys_com)
    result = f'OK: system command "{command}"'

    return result


def process_cd(command: str) -> str:
    # требуемая директория
    need_dir = re_sub('\s', ' ', command[2:]).strip()
    # перемещение
    result = cd_command.main_cd(need_dir=need_dir)

    return result


def process_ls(command: str) -> str:
    filelist = ls_command.show_cur_dir_content()
    print(filelist)
    result = f'OK: {command}'

    return result


def process_pwd(command: str) -> str:
    dir_path = pwd_command.show_cur_dir_path()
    print(dir_path)
    result = f'OK: {command}'

    return result


def process_mkdir(command: str) -> str:
    # неподдерживаемые символы
    except_symbols = '[\/:*\\\<>+|\'\"?,]'

    name_new_dir = re_sub('\s', ' ', command[5:]).strip()
    if re_findall(except_symbols, name_new_dir):
        result = 'ERROR: your dirname contain unsupported symbols!'
    else:
        result = mkdir_command.make_new_dir(name_new_dir)

    return result


def process_rename(command: str) -> str:
    # неподдерживаемые символы
    except_symbols = '[\/:*\\\<>+|\'\"?,]'

    # извлекаем из команды старое и новое имя для директории
    names_list = re_sub('\s', ' ', command[6:]).split(' ./')[1:]

    if len(names_list) == 2:
        old_name = names_list[0].strip()
        new_name = names_list[1].strip()

        # если новое имя содержит неподдерживаемые символы
        if re_findall(except_symbols, new_name):
            result = 'ERROR: your new dirname contain unsupported symbols!'
        else:
            result = rename_command.rename_file(old_name=old_name, new_name=new_name)
    else:
        result = 'ERROR: invalid names count!'

    return result


def process_get(command: str) -> str:
    clear_command = re_sub('\s|(\./)', ' ', command[3:]).strip()

    if clear_command.startswith('-r'):
        return 'ERROR: пока не сделал'
    else:
        # требуемый файл
        need_file = clear_command
        # скачивание
        result = get_command.download_file(file_name=need_file)

    return result


def process_put(command: str) -> str:
    clear_command = re_sub('\s', ' ', command[3:]).strip()

    if clear_command.startswith('-r'):
        return 'ERROR: пока не сделал'
    else:
        # требуемый файл
        need_file_with_path = clear_command
        # полный путь с именем файла
        path = abspath(need_file_with_path)
        print([path])

        # если такого файла не существует
        if not exists(path):
            return 'ERROR: such file not exists!'

        # проверка на файл
        if isfile(path):
            file_name = path.split('/')[-1]
            # загрузка
            result = put_command.upload_file(file_name=file_name, path=path)
        else:
            return 'ERROR: to upload dir add key "-r"'

    return result


# обработка команд и распределение задач
def process_manage(command: str) -> str:
    # словарь с доступными командами
    command_dir = {
        'help': process_help,
        '!': process_sys,
        'cd': process_cd,
        'ls': process_ls,
        'pwd': process_pwd,
        'mkdir': process_mkdir,
        'rename': process_rename,
        'get': process_get,
        'put': process_put,
    }

    try:
        # название вызываемой команды
        command_word = '!' if command.startswith('!') else command.split()[0]
    # нажатый Enter
    except IndexError:
        return 'OK: Enter'

    # выполнение команды
    try:
        feedback = command_dir[command_word](command=command)
    # если команды нет в словаре
    except KeyError:
        feedback = 'ERROR: invalid command!'
    except Exception as error:
        return f'FATAL!!!\nWhile processing command "{command}" you got error:\n{error}'

    return feedback
