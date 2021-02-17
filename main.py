import update
import parse
import json
import time
import logs

interval = 30
logger = logs.get_logger("sleep")


def working():
    data = update.get()
    parse.parse_data(data=data)
    logger.info("WAITING...")
    time.sleep(interval)
    while(1):
        data = update.get()
        parse.parse_new_data(data=data)
        logger.info("WAITING...")
        time.sleep(interval)


if __name__ == "__main__":
    working()