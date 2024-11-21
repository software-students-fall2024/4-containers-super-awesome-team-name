"""
Unit tests for app.py web app.
"""

from unittest import mock
import pytest
from app import app


@pytest.fixture
def app_client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client


def test_index_route(app_client):
    """Test the index route."""
    res = app_client.get("/")
    assert res.status_code == 200
    assert b"Sound Analyzer" in res.data


def test_analyze_route(app_client):
    """Test the analyze route."""
    res = app_client.get("/analyze")
    assert res.status_code == 200
    assert b"Tap to Listen" in res.data


@mock.patch("app.collection.insert_one")
def test_save_result(mock_insert_one, app_client):
    """Test saving the classification result."""

    # mocking the data, see ackowledgements in the README
    mock_data = {"classification": "clapping", "timestamp": "2024-11-17T12:00:00"}
    res = app_client.post("/save_result", json=mock_data)
    assert res.status_code == 200
    assert res.json["status"] == "success"
    mock_insert_one.assert_called_once_with(mock_data)


@mock.patch("app.collection.insert_one")
def test_save_result_no_data(mock_insert_one, app_client):
    """Test saving classification result but with no data."""
    res = app_client.post("/save_result", json={})
    assert res.status_code == 400
    assert res.json["status"] == "error"
    assert "No data received" in res.json["message"]

    # assertion for the mock, see ackowledgements in the README
    mock_insert_one.assert_not_called()


@mock.patch("app.collection.find")
def test_results_route(mock_find, app_client):
    """Test the results route."""

    # mock for the return, see ackowledgements in the README
    mock_find.return_value = [
        {"_id": "1", "classification": "clapping", "timestamp": "2024-11-17T12:00:00"}
    ]
    res = app_client.get("/results")
    assert res.status_code == 200
    assert b"Classification Result" in res.data


@mock.patch("app.collection.delete_one")
@mock.patch("app.ObjectId")
def test_delete_result(mock_id, mock_delete_one, app_client):
    """Test to delete a classification result."""
    # Generic obj ID
    result_id = "507f1f77bcf86cd799439011"
    # mock return, see ackowledgements in the README
    mock_id.return_value = result_id

    res = app_client.post(f"/delete_result/{result_id}")
    # Redirect
    assert res.status_code == 302

    # assertions for the mocks, see ackowledgements in the README
    mock_id.assert_called_once_with(result_id)
    mock_delete_one.assert_called_once_with({"_id": result_id})
