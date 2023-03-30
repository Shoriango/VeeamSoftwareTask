import os
import filecmp
import shutil
import time
import datetime


def delete_file(path):
    """
    Deletes a file/folder given the path
    :param path: Path of the file/folder to be deleted
    :return:
    """
    if os.path.isfile(path):
        os.remove(path)
        return
    elif os.path.isdir(path):
        shutil.rmtree(path)
        return


def copy_file(source_file, replica_file):
    """
    Copies a file/folder into a destination
    :param source_file: Path of the file to be copied
    :param replica_file: Path that the file will be copied into
    :return:
    """
    if os.path.isfile(source_file):
        shutil.copy2(source_file, replica_file)
    elif os.path.isdir(source_file):
        os.makedirs(replica_file)
        sync_folders(source_file, replica_file)


def file_log(message):
    """
    Writes a message in Replica_Log_File.txt
    :param message: Message to be written
    :return:
    """
    with open('Replica_Log_File.txt', 'a') as file:
        file.write(f'{message}\n')
        file.close()


def get_current_time():
    """
    Gets the current time with the following format:
    Year-Month-Day Hour:Minute:Second
    :return: Returns the date and time in a string
    """
    date = datetime.datetime.now()

    return f"{date.year}-{date.month}-{date.day} " \
           f"{date.hour}:{date.minute}:{date.second}"


def sync_folders(source, replica):
    """
    Function used to synchronize two folders, copying and deleting any items
    necessary
    :param source: Path of the folder to be replicated
    :param replica: Path for the source to be duplicated into
    :return:
    """
    if not os.path.exists(source):
        print(" \n The source path doesn't exist")
        return

    if not os.path.exists(replica):
        os.makedirs(replica)

    comp_folders = filecmp.dircmp(source, replica)
    source_files = comp_folders.left_list
    replica_files = comp_folders.right_list
    same_dirs = comp_folders.common_dirs
    same_files = comp_folders.same_files

    for file in replica_files:
        if file not in same_files and file not in same_dirs:
            delete_file(os.path.join(replica, file))
            file_log(f"{file} was deleted from {replica}"
                     f" at {get_current_time()}")
    for file in source_files:
        if file not in same_files and file not in same_dirs:
            copy_file(os.path.join(source, file), os.path.join(replica, file))
            file_log(f"{file} was copied into {replica} "
                     f"at {get_current_time()}")

    for folder in same_dirs:
        sync_folders(os.path.join(source, folder),
                     os.path.join(replica, folder))


def main():
    """
    Is called when the program is executed, first asking the source folder,
    Then the replica folder and the synchronization time in minutes.
    :return:
    """
    src_path = input('Insert the path of the folder you want to replicate: ')
    rep_path = input('Insert the path for the folder to be replicated to: ')
    minutes = int(input('Insert the interval of time '
                        'for the folder to be updated (in minutes): '))

    while True:
        try:
            sync_folders(src_path, rep_path)

            print(f'Updated at {get_current_time()}')
            time.sleep(minutes * 60)
        except OSError:
            print("Check if both inserted paths are correct")
            input('Press enter to exit program')
            return


if __name__ == "__main__":
    main()
