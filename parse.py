import db
import logs

logger = logs.get_logger("db")


def parse_new_data(data):
    currency = data["data"]
    for current in currency:
        db.update(str(current["name"]), current["quote"]["USD"]["price"])
    logger.info("DB WAS UPDATED")
    db.join()
    logger.info("HISTORY WAS UPDATED")


def parse_data(data):
    currency = data["data"]
    for current in currency:
        db.insert((str(current["name"]), current["quote"]["USD"]["price"]))
    logger.info("DB WAS CREATED")
    db.insert_history()
    logger.info("HISTORY WAS CREATED")