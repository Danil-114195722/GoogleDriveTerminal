from work_with_state.dir_content_writter import get_list_content


# вывод содержимого текущего каталога
def show_cur_dir_content() -> str:
    # список с папками и файлами
    list_content = get_list_content()

    # кол-во файлов и папок в данной директории
    num_dir = num_file = 0

    # преобразуем контент в строку
    str_content = ''
    for elem in list_content:
        str_content += '\n' + elem[0] + ' -- ' + elem[1]
        # подсчёт кол-ва папок и файлов
        if elem[0] == 'dir':
            num_dir += 1
        else:
            num_file += 1

    # объединяем основной контент с кол-вом элементов
    cool_table = f'All: {num_dir + num_file} || Dirs: {num_dir} || Files: {num_file}' + str_content

    return cool_table
