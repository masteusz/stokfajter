import datetime
import json
import logging

import const


def configure_logger(logger=logging.getLogger('stockfighter')):
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


class StockFighterApiClient:
    def __init__(self, logger_name, account, apikey=None):
        self.logger = logging.getLogger(logger_name + '.stockFighter')
        self.logger.debug("Initializing StockFighterApiClient")
        self._base_url = "https://api.stockfighter.io/ob/api"
        self.account = account
        self.apikey = apikey
        if apikey is None:
            self.apikey = self.load_api_key_from_file(filename=const.API_KEY_FILENAME)
            self.logger.debug("Loaded API key from file: %r", self.apikey)

    def heartbeat_api(self):
        raise NotImplementedError

    def load_api_key_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                to_parse = f.readline()
                try:
                    parsed = json.loads(to_parse)
                    return parsed.get("apikey")
                except ValueError as err:
                    self.logger.error("Error while reading JSON: %r", err)
        except FileNotFoundError as err:
            self.logger.error("File not found: %r", err)


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    logger = logging.getLogger('sf')
    configure_logger(logger)
    logger.info('SCRIPT STARTED')

    sf = StockFighterApiClient(logger_name="sf", account="")

    logger.info('SCRIPT FINISHED')
    logger.info('Time elapsed: %s', datetime.datetime.now() - start_time)
    logger.info('-' * 60)
