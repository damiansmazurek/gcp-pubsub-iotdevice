import uuid
import time
import json
from connector import PubSubConnector

class DeviceEmulator:
    def __init__(self, project_id, topic_name):
        self.client = PubSubConnector(project_id, topic_name)
        #create device id
        self.deviceId = uuid.uuid4()

    def send_data(self, data):
        message = {"deviceid": self.deviceId, "timestamp": time.time(), "data": data}
        self.client.sendMessage(json.dumps(message))
        