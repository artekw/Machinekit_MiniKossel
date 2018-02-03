#!/usr/bin/python

import sys
import os
import subprocess
import importlib
from machinekit import launcher
from time import *


launcher.register_exit_handler()
#launcher.set_debug_level(5)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    launcher.check_installation()
    launcher.cleanup_session()
    launcher.load_bbio_file('cramps2_cape.bbio')
    launcher.start_process('videoserver --ini ~/videoserver/video.ini Webcam1') 
    launcher.start_process("configserver -n MiniKossel ~/Machineface ~/Cetus/")
    launcher.start_process('linuxcnc CRAMPS.ini')
#    launcher.start_process("python lcd.py");
except subprocess.CalledProcessError:
    launcher.end_session()
    sys.exit(1)

# loop until script receives exit signal
# or one of the started applications exited incorrectly
# cleanup is done automatically
while True:
    sleep(1)
    launcher.check_processes()
