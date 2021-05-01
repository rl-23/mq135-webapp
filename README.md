# mq135-webapp<br/>
Repo for my teentech project. <br/>
MQ135 takes readings of the indoor air quality in ppm, and the flask server displays the ppm, and the safety level of the air.

# guide for the files: <br/>
ADUINO_WITH_MQ135.ino: This is the code for the arduino. It runs on the arduino(pro micro) and gives us a ppm reading. <br/> <br/>
datarecieve.py: This python file recives the data from the arduino via serial. Furthermore, it formats the data so it is only an integer and can be processed easily. <br/><br/>
servermain.py: This is the setup for the flask server. This is where the web app comes from.</br></br>
index.html and all files in 'static' and 'templates': link to the flask server. This is the html, css, js, and img files for our website. They are in this format as this is the structure that flask reads files.
