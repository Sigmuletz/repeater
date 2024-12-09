import logging

threads = 10

# Logging Prep
logger = logging.getLogger("Logging")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("rep.log", mode="a", encoding="utf-8")

formatter = logging.Formatter("{asctime} [{levelname}] : {message}", style="{", datefmt="%Y-%m-%d %H:%M:%S")

console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

### START ###
#############
logger.warning("------------")
logger.warning("... Star ...")
###



###
logger.warning("... Stop ...")