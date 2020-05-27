import subprocess
import time

stillsDir = "~/Desktop/cameraShots/"
vidsDir = "~/Desktop/cameraVids/"

def photo():
    epoch_time = int(time.time())
    takeStill = subprocess.run(["raspistill", "-o stillsDir%d.jpg" % epoch_time])

# takeVid = subprocess.run(["raspistill", "-o stillsDir%d.jpg" % epoch_time])

