import pytest
import requests
from mock import MagicMock

from stockfighter_api_client import stockfighter_api_client


class MockedResponse:
    def __init__(self, json, status_code):
        self.status_code = status_code
        self.jsondict = json

    @staticmethod
    def raise_for_status():
        raise Exception

    def json(self):
        return self.jsondict


@pytest.fixture()
def stockfighter():
    sf = stockfighter_api_client.StockFighterApiClient(account="", logger_name="")
    return sf


def test_correct_response(stockfighter):
    m = MockedResponse(status_code=200, json={"ok": True})
    requests.get = MagicMock(return_value=m)
    res = stockfighter.heartbeat_venue("TESTVENUE")
    assert res is True


def test_error_response(stockfighter):
    m = MockedResponse(status_code=404, json={"ok": False})
    requests.get = MagicMock(return_value=m)
    with pytest.raises(Exception) as exc_info:
        res = stockfighter.heartbeat_venue("TESTVENUE")

