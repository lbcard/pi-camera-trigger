

# Basic start script which works......
source cam-trigger/pi-camera-trigger-env/bin/activate
cd ~/Desktop/cam-trigger/pi-camera-trigger/ 
flask run --host 0.0.0.0 --port 5000
##########################################





# check stuff


# build scripts

## mk env dir and code dir
## clone code dir
## activate env
## un webserver
mkdir  
source ~/Desktop/cam-trigger/pi-camera-trigger-env/bin/activate
cd ~/Desktop/cam-trigger/pi-camera-trigger
pip3 install flask
# maybe set bashrc bashprofile
export FLASK_APP=app.py
flask run --host=0.0.0.0