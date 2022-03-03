import time
import shutil
import os


def  deleteTheFolder():

    path = input("Which folder would you like to delete? ")

    days = 0

    seconds = time.time() - (days*60*60)

    if os.path.exists(path):

        if seconds > get_file_or_folder_age(path) :

            if not shutil.rmtree(path):
                print("The mentioned file/folder has been deleted!")

            else:
                print("Unable to Delete")



def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime



deleteTheFolder()