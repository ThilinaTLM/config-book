#! /usr/bin/python3
import os
import sys

def urlList():
    if (len(sys.argv) > 1):
        filepath = sys.argv[1]
    else:
        print("No download list is provided!")
        exit()
    
    content = []
    try:
        content = open(filepath, 'r').read()
    except:
        print("Error while reading the file.")
        exit()
    
    return filter(lambda u: len(u.replace(' ', '')) > 0, content.split("\n"))

def downloadFile(url):
    os.system("axel {}".format(url))

for url in urlList():
    print("Start downloading... {}".format(url))
    downloadFile(url)
    print("Finished! {}".format(url))

print("All done!")

