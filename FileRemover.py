
######################################################################################
#__Purpose__    = "To remove old files from folder based on a pattern"               #
#__Platform__	= "Python"                                                           #
#__File.Name__  = "File_Remover.py"                                                  #
#__Updated__    = "24th October 2015"                                                #
######################################################################################


import sys
import os
import datetime
import time

date_now= datetime.datetime.now().strftime("%y%m%d")
month=date_now[2:4]
day=date_now[4:]
year=date_now[0:2]

print (day, month, year)

folderPath = "/home/testFolder"

## Set path to that of the desired dropbox folder
for path, subdirs, files in os.walk(folderPath):
   for filename in files:
        a = filename
	## Removes .mp4, .MP4, .jpg, JPG file types
        if a[len(a)-4:].lower() == ".mp4" or a[len(a)-4:].lower() == ".jpg":
             print filename
             date_file= a.replace(' ','a').replace('.','*').replace('_','*').split('*')
             print date_file
             print len(date_file)
             if len(date_file)>2:
                 print date_file
                 date_file=date_file[1]
                 if int(date_file[0:2]) < int(year):
                    os.remove(folderPath+filename)
                 else:
                     if int(date_file[2:4]) < int(month):
                         os.remove(folderPath+filename)
                     else:
                         if int(date_file[4:]) < int(day):
                             os.remove(folderPath+filename)


sys.exit (0)
