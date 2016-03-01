import logging

import datetime


def configure_logger(logger=logging.getLogger('stockfighter')):
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


class StockFighterApiClient:
    def __init__(self, logger_name):
        self.logger = logging.getLogger(logger_name + '.stockFighter')
        self.logger.debug("Initializing StockFighterApiClient")
        self._base_url = "https://api.stockfighter.io/ob/api"


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    logger = logging.getLogger('sf')
    configure_logger(logger)
    logger.info('SCRIPT STARTED')

    sf = StockFighterApiClient(logger_name="sf")

    logger.info('SCRIPT FINISHED')
    logger.info('Time elapsed: %s', datetime.datetime.now() - start_time)
    logger.info('-' * 60)


