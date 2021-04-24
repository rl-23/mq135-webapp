# mq135-webapp<br/>
Repo for my teentech project. <br/>
MQ135 takes readings of the indoor air quality in ppm, and the flask server displays the ppm, and the saftey level of the air.

Guide for the files: <br/>
ADUINO_WITH_MQ135.ino: This is the code for the arduino. It runs on the arduino(pro micro) and gives us a ppm reading. <br/>
datarecieve.py: This python file recives the data from the arduino via serial. Furthermore, it formats the data so it is only an integer and can be processed eaily.
