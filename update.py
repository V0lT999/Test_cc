from requests import Request, Session
import json
import logs

logger = logs.get_logger("requests")


def exception_status_code(status_code):
    if status_code == 102:
        logger.info("CODE 102: PROCESSING")
    elif status_code == 400:
        logger.info("CODE 400: BAD REQUEST")
    elif status_code == 401:
        logger.info("CODE 401: UNAUTHORIZED")
    elif status_code == 403:
        logger.info("CODE 403: FORBIDDEN")
    elif status_code == 404:
        logger.info("CODE 401: NOT FOUND")
    elif status_code == 405:
        logger.info("CODE 405: METHOD NOT ALLOWED")
    elif status_code == 408:
        logger.info("CODE 401: REQUEST TIMEOUT")
    else:
        logger.info("REQUEST ERROR")


def get():
    logger.info("GET-REQUEST")

    try:
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '10',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '3532c9f2-8fb3-4ebb-8472-01186fb5b386',
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            logger.info("STATUS: OK!")
            return data
        except:
            exception_status_code(response.status_code)
    except:
        logger.info("SMTH WRONG")