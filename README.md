# PythonFileRemover
Remove files from a folder using python 

#Naming Convention:
All the video files (.mp4) and image files (.jpg or .JPG) should be named as follows: <br/>
Firstpart_yymmdd.mp4    or   firstpart_yymmdd.jpg <br/>
First part- can be any length of character without any space or symbols like dollar sign ($), period (.), comma (,), and <br/> underscore (_). Refrain from using any special symbols to name the first part.<br/>

#Allowed: 
Slide1_141118.jpg<br/>
TinaIsComingToMarylandon2nd_141001.mp4<br/>

#Not Allowed:
Slide1$ 2nd_141108.jpg     X   (Dollar sign and space shouldn’t come in the first part)<br/>
Slide Tomorrow.mp4         X   (Space isn’t allowed)<br/>
abcC._141109.jpg           X    (Period is not allowed)<br/>
abc1egh~`_141110.mp4       X  (Special symbols aren’t allowed in the name)<br/>

#Date Format:
mm- Single digit months should be prefixed with a 0. Eg. 01, 02<br/>
yy- two digits <br/>
dd- same as months <br/>
(Note: yymmdd – The date when the slide needs to be deleted from the system. (Usually, the next day of the event)<br/>
