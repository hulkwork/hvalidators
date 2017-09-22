import hazelcast, logging
from conf import settings

config = hazelcast.ClientConfig()
# Hazelcast.Address is the hostname or IP address, e.g. 'localhost:5701'
if "hazelcast-adress" in settings:
    for node in settings["hazelcast-adress"]:
        config.network_config.addresses.append(settings["hazelcast-adress"][node])
else:
    config.network_config.addresses.append("localhost:5701")

# basic logging setup to see client logs
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler(settings['log-location'])
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.info("Let's begin hazelcast python client")
client = hazelcast.HazelcastClient(config)
