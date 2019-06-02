import shutil
import os


def file_movedir(filename,dir_name):
    dir_path = "D:/final/backend/data"
    if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

    if not os.path.isdir(dir_path+"/"+dir_name):
            os.mkdir(dir_path+"/"+dir_name)

    shutil.move("D:/final/backend/media/" +filename, dir_path + "/" + dir_name + "/" + filename)