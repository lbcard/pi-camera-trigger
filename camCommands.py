import subprocess
import time

stillsDir = "~/Desktop/cameraShots/"
vidsDir = "~/Desktop/cameraVids/"

def photo():
    epoch_time = int(time.time())
    takeStill = subprocess.run(["raspistill", "-o stillsDir%d.jpg" % epoch_time])
    print ("takeStill response: ")
    print (takeStill)
    return "Photo Triggered %d.jpg" % epoch_time

    # if :
    #     return "Photo Triggered"
    # else:
    #     return "Fault Taking Photo"

# takeVid = subprocess.run(["raspistill", "-o stillsDir%d.jpg" % epoch_time])

