#!/home/danil/anaconda3/envs/stable/bin/python


from re import sub as re_sub

from work_with_state.current_dir_writter import get_cur_dir
from processes import cd_command, ls_command


# обработка команд и распределение задач
def process_manage(command: str) -> None:
    # команда "cd"
    if command.startswith('cd'):
        # требуемая директория
        need_dir = re_sub('\s|(\./)', ' ', command[2:]).strip()

        # идём в рута
        if need_dir == '/':
            feedback = cd_command.move_to_root()
        # идём на уровень ниже
        elif need_dir == '..':
            feedback = cd_command.move_one_step_down()
        # идём в следующий указанный каталог
        else:
            feedback = cd_command.move_to_dir(dir_name=need_dir)

    elif command == 'ls':
        feedback = 'OK: ls'
        filelist = ls_command.show_cur_dir_content()
        print(filelist)

    elif command == '':
        return
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
