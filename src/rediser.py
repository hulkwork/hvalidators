import redis
import pickle
import conf
import logging
import pymongo
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler(conf.settings['log-location'])
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.info("Let's begin redis python client")


class StrictRedisMongo(redis.StrictRedis):
    def __init__(self, **kwargs):
        self.conf_mongo = kwargs.get("conf_mongo", None)
        redis.StrictRedis.__init__(self)

    def save(self):
        if not self.conf_mongo:
            redis.StrictRedis.save(self)
        else:
            # TODO: save into mongodb
            return None


redis_mongo = StrictRedisMongo(host=conf.CONFIG_REDIS["host"], port=conf.CONFIG_REDIS["port"],
                               conf_mongo=conf.CONFIG_MONGO)
