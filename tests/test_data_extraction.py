from data_extraction.extract_initial import extract_initial_data
from data_extraction.extract_refresh import extract_refresh_data

def test_initial_data_extraction():
    data = extract_initial_data()
    assert len(data) > 0

def test_refresh_data_extraction():
    data = extract_refresh_data()
    assert len(data) > 0

