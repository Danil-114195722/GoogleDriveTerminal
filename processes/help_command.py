def show_help_manual() -> str:
    help_content = '''SUPPORTED COMMANDS:

    1-->  ! "sys command"
    2-->  ls
    3-->  pwd
    4-->  cd "path"
    5-->  mkdir "name"
    6-->  rename ./"old_name" ./"new_name"
    7-->  put "name"
    8-->  get "name"
    9-->  "command 1" && "command 2"
    10->  "command 1" && \\
         "command 2" && "command 3"

SAMPLES:

    1-->  Input:
                ! ls
          Output: (list of files and dirs for current dir on your PC)
                test1 my_dir large_file.txt cat.png
    2-->  Input:
                ls
          Output: (list of files and dirs for current dir on your Google Drive Account)
                All: 3 || Dirs: 1 || Files: 2
                dir -- test1
                file -- cat.png
                file -- document.docx
    3-->  Input:
                pwd
          Output: (full path to current dir on your Google Drive Account)
                /full/path/to/current/dir
    4-->  Input:
                cd ./MyDocs
          Output: (move to dir "MyDocs" from current dir ("./") on your Google Drive Account)
                (None)
    5-->  Input:
                mkdir new_dir
          Output: (create dir in current dir on your Google Drive Account)
                (None)
    6-->  Input:
                rename ./new_dir ./my_secret_info
          Output: (rename dir "new_dir" to "my_secret_info" on your Google Drive Account)
                (None)
    7-->  put "name"
    8-->  get "name"
    9-->  "command 1" && "command 2"
    10->  "command 1" && \
        "command 2" && "command 3"
'''

    return help_content
