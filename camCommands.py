import os
import time
from PIL import Image

vidsDir = "~/Desktop/cameraVids/"


def photo():
    stillsDir = "./static/images/"
    epoch_time = int(time.time())
    # takeStill = subprocess.run(["raspistill", "-o %s%d.jpg" % (stillsDir, epoch_time)])
    takeStill = os.system("raspistill -o %s%d.jpg" % (stillsDir, epoch_time))
    print("takeStill response: ")
    print(takeStill)
    return ["Photo Triggered %d.jpg" % epoch_time, epoch_time]

    # if :
    #     return "Photo Triggered"
    # else:
    #     return "Fault Taking Photo"

# takeVid = subprocess.run(["raspistill", "-o stillsDir%d.jpg" % epoch_time])


def createProxy(inputImage, directory):
    basewidth = 300
    img = Image.open(directory + inputImage)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    inputImageName = inputImage[:-4]
    img.save(directory + "/imageProxies/" + inputImageName + "_small" + ".jpg")
