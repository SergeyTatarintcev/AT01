import pytest
from main import get_random_cat_image
import requests

def test_success_response(mocker):
    mock_data = [{"url": "https://cdn.thecatapi.com/images/test123.jpg"}]
    mock_response = mocker.Mock(status_code=200, json=lambda: mock_data)
    mocker.patch("requests.get", return_value=mock_response)

    result = get_random_cat_image()
    assert result == "https://cdn.thecatapi.com/images/test123.jpg"


def test_not_200_response(mocker):
    mock_response = mocker.Mock(status_code=404)
    mocker.patch("requests.get", return_value=mock_response)

    result = get_random_cat_image()
    assert result is None


def test_request_exception(mocker):
   
    mocker.patch("requests.get", side_effect=requests.RequestException("Network error"))

    result = get_random_cat_image()
    assert result is None

