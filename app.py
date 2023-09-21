#!/home/danil/anaconda3/envs/stable/bin/python


from re import sub as re_sub

from work_with_state.current_dir_writter import get_cur_dir
from processes import (cd_command, ls_command, pwd_command,
                       mkdir_command, rename_command,
                       system_interaction)


# обработка команд и распределение задач
def process_manage(command: str) -> None:
    # нажатый Enter
    if command == '':
        return
    # любая системная команда
    elif command.startswith('!'):
        sys_com = command[1:]
        system_interaction.system_command_exec(command=sys_com)
        feedback = 'OK: system command'

    # команда "cd"
    elif command.startswith('cd'):
        # требуемая директория
        need_dir = re_sub('\s', ' ', command[2:]).strip()
        # перемещение
        feedback = cd_command.main_cd(need_dir=need_dir)

    elif command.startswith('ls'):
        feedback = 'OK: ls'
        filelist = ls_command.show_cur_dir_content()
        print(filelist)

    elif command.startswith('pwd'):
        feedback = 'OK: pwd'
        dir_path = pwd_command.show_cur_dir_path()
        print(dir_path)

    elif command.startswith('mkdir'):
        name_new_dir = re_sub('\s', ' ', command[5:]).strip()
        feedback = mkdir_command.make_new_dir(name_new_dir)

    elif command.startswith('rename'):
        old_name, new_name = re_sub('\s', ' ', command[6:]).strip().split(' ')
        feedback = rename_command.rename_file(old_name=old_name, new_name=new_name)

    else:
        feedback = 'ERROR: invalid command!'

    # печатаем только ошибки
    if feedback.startswith('ERROR'):
        print(feedback)


def main() -> None:
    # по дефолту переходим в корень диска
    cd_command.move_to_root()

    while True:
        try:
            # считывание введённой команды
            command = input(f'drive{":" + get_cur_dir()}> ').strip()
        # выход из программы
        except KeyboardInterrupt:
            print('\nGoodbye!')
            break

        # выход из программы
        if command == 'exit' or command == 'quit':
            print('Goodbye!')
            break

        # обработка команды
        process_manage(command=command)


if __name__ == '__main__':
    main()
