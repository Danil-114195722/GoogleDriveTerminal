# запись текущей директории
def set_cur_dir(directory: str) -> None:
    with open('./state/current_dir', 'w') as file_cur_dir:
        file_cur_dir.write(directory)


# получение текущей директории
def get_cur_dir() -> str:
    with open('./state/current_dir', 'r') as file_cur_dir:
        cur_dir = file_cur_dir.read()
    return cur_dir
