import pytest
from service import scraper
import time

def test_create_stock_json():
    got_data = scraper.create_stock_json_record()
    time.sleep(10)
    print(got_data)
    assert got_data
