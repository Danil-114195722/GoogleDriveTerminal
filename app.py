#!/home/danil/anaconda3/envs/stable/bin/python


from work_with_state.current_dir_writter import get_cur_dir
from processes import cd_command, process_manager


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

        # обработка команды м получение ответа выполнения
        feedback = process_manager.process_manage(command=command)

        # печатаем только ошибки
        if feedback.startswith('ERROR') or feedback.startswith('FATAL'):
            print(feedback)


if __name__ == '__main__':
    main()
