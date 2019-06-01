import shutil
import os


def file_movedir(file_ex,dir_name):
    dir_path = "D:/backend_test/data"
    if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

    if not os.path.isdir(dir_path+"/"+dir_name):
            os.mkdir(dir_path+"/"+dir_name)

    shutil.move("D:/backend_test/media/" +file_ex, "D:/backend_test/data" + "/" + dir_name + "/" + file_ex)