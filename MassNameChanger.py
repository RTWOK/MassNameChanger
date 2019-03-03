import os
from datetime import datetime




def renamefiles(path_to_old_file):
    os.chdir(path_to_old_file)
    userName = input("Enter the name you want your files to have: ")
    userExtension = input("Enter the file extension you want to target(such as .mp4 etc): ")
    #if userName + userExtension == "":
        #print("You can't just have nothing as your file name")
    print("\n")
    Log = open("renameLog.txt", "w")
    startTime = datetime.now()



    for item in os.listdir():  #for every item in the directory
        tries = 0  #set tries to 0
        item_name, item_extension = os.path.splitext(item)  #split item extension off and store name and extension in specified
        old_item_name = item #save the current item
        if item_extension == userExtension:  #if the item_extension is ".mp4"
            new_item_name = str(tries) + " " + userName + item_extension  #set newName to specified
            while new_item_name in os.listdir():  #while newName is in directory
                tries = tries + 1  #increment tries by 1
                new_item_name = str(tries) + " " + userName + item_extension  #set newName to specified
            os.rename(item, new_item_name)  #rename the current item to newName
            print("[" + old_item_name + "]" + " turned to -> " + "[" + new_item_name + "]" + "\n")
            Log.write("[" + old_item_name + "]" + " turned to -> " + "[" + new_item_name + "]" + "\n")  #note down the change you made to the file
        else:
            if item_extension == "":
                if item_name == "renameLog":
                    continue
                else:
                    print("-- " + item + " has no extension. Is it a folder perhaps?" + "\n")
            else:
                if item_name == "renameLog":
                    continue
                else:
                    print("-- I also found " + item + " which has " + item_extension + " as extension. It has not been changed." + "\n")
    Log.close()
    print(datetime.now() - startTime)

def start_renameFiles():
    try:
        renamefiles(input("Enter the Path of the files you want to mass rename: "))
    except:
        print("Oopsie! Something went wrong. Try again.(Make sure you enter a valid path and your target extension and filename are not identical.)")
        start_renameFiles()

start_renameFiles()
print("Finished: ")

