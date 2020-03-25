#-------------------------------------------------------------------------
# Copyright (c) Chmurowisko. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import os
import time
from logging import log, info, debug, basicConfig, DEBUG, INFO
from random import seed, random
from emulator import DeviceEmulator

#logging configuration
basicConfig(format='%(asctime)s; %(levelname)s: %(message)s', level=INFO)

# Get env variables
info('Global variables uploaded')
PROJECT_ID = os.environ.get('PROJECT_ID')
TOPIC_NAME = os.environ.get('TOPIC_NAME')
WINDOW_SIZE = int(os.environ.get('WINDOW_SIZE'))
WINDOW_INTERVAL = int(os.environ.get('WINDOW_INTERVAL'))
TIME_INTERVAL = int(os.environ.get('TIME_INTERVAL'))

# Create emulator
info('Creating device emulator')
emulator = DeviceEmulator(PROJECT_ID, TOPIC_NAME)
info('Start sending events, window size: %d s',WINDOW_SIZE )
while True:
    time_to_live = time.time()
    info('Start sending window')
    while (time.time()-time_to_live < WINDOW_SIZE):
        seed(time.time())
        entity = {"I": 100* random(), "U": 30* random()+210, "Tm": 150* random() }
        info('Sending data: %s',str(entity))
        result = emulator.send_data(entity)
        time.sleep(TIME_INTERVAL)
        info('Entity sended with result %s', str(result))
    info('Sending window ended - waiting for next %d s',WINDOW_INTERVAL)
    time.sleep(WINDOW_INTERVAL)
        

    