#! /usr/bin/python3

from os import listdir, getcwd, system
from os.path import join, isfile, isdir, abspath
from sys import argv

destinations = [
        "/mnt/180371K/",
        "/mnt/180479A/"
]

def main(rootSrc = ".", rootDest = "/mnt/"):
    absSrc = abspath(rootSrc)
    absDest = abspath(rootDest)
    
    if not isdir(absDest):
        print("Destination directory must exist, {}".format(absDest))
        exit()
    
    source_files = []
    if isfile(absSrc):
        source_files.append(absSrc)
    elif isdir(absSrc):
        source_files = chooseSource(absSrc)
    else:
        print("Source file or directory must exits, {}".format(absSrc))
        exit()
    
    dest_directory = chooseDestination(absDest)
        
    print("PROCESSING...")
    for source in source_files:
        system("rsync -ah --progress '{}' '{}'".format(source, dest_directory))
    print("FINISHED")

def chooseSource(cwd):
    files, _ = readNodeList(cwd)
    print("[SELECT SOURCE]")
    choices = getUserChoice(files)
    if choices == 0: exit()
    return [join(cwd, choice) for choice in choices]

def chooseDestination(path):
    print("[SELECT DESTINATION]")
    print(' ', path)
    while True:
        _, folders = readNodeList(path)
        if folders == []:
            return path
        choices = getUserChoice(folders)
        if choices == 0:
            return path
        if len(choices) > 1:
            print("Mutiple choices detected! but use first one.")
        path = join(path, choices[0])

def readNodeList(path):
    files = []
    folders = []
    # find files and folders
    for node in listdir(path):
        if isdir(join(path, node)):
            folders.append(node)
        else:
            files.append(node)
    
    return [files, folders]

def getUserChoice(list):
    for ind, item in enumerate(list):
        print("    [{}]: {}".format(ind+1, item))
    while True:
        inp = input("choice: ") 
        if inp == '' or list == []:
            return 0
        elif inp == '*':
            return list
        try:
            return [list[int(i) - 1] for i in inp.split()]
        except:
            print("    > Cannot parse your input <")

                    
if __name__ == "__main__":
    if len(argv) > 2:
        main(argv[1], argv[2])
    elif len(argv) > 1:
        main(argv[1])
    else:
        main()
