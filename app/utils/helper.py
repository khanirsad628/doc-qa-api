import os

def size_in_mb(size:int):
    return size/(1024*1024)

def create_folder(folder_name):
    os.makedirs(folder_name,exist_ok=True)