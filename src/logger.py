import logging.config


logging.config.fileConfig("./logging.conf")

log = logging.getLogger()
