import os
import shutil

from nio_colmap.Method.path import removeFile

def copyFile(rel_file_path):
    source_file_path = '../niocm/' + rel_file_path
    target_file_path = './nio_colmap/Cpp/' + rel_file_path

    if not os.path.exists(source_file_path):
        print('[ERROR][replace::copyFile]')
        print('\t source file not exist!')
        print('\t source_file_path:', source_file_path)
        return False

    if not os.path.exists(target_file_path):
        print('[ERROR][replace::copyFile]')
        print('\t target file not exist!')
        print('\t target_file_path:', target_file_path)
        return False

    removeFile(source_file_path)
    shutil.copyfile(target_file_path, source_file_path)
    return True

def copyFolder():
    target_folder_path = './nio_colmap/Cpp/'

    for root, _, files in os.walk(target_folder_path):
        if len(files) == 0:
            continue

        for file_name in files:
            rel_file_path = root.replace(target_folder_path, '') + '/' + file_name
            print(rel_file_path)

            copyFile(rel_file_path)
    return True
