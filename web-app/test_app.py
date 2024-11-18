"""
Unit tests for app.py web app.
"""

from unittest import mock
import pytest
from app import app


@pytest.fixture
def setup_client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client


def test_index_route(app_client):
    """Test the index route."""
    response = app_client.get("/")
    assert response.status_code == 200
    assert b"Sound Analyzer" in response.data


def test_analyze_route(app_client):
    """Test the analyze route."""
    response = app_client.get("/analyze")
    assert response.status_code == 200
    assert b"Tap to Listen" in response.data


@mock.patch("app.collection.insert_one")
def test_save_result(mock_insert_one, app_client):
    """Test saving a classification result."""
    mock_data = {"classification": "clapping", "timestamp": "2024-11-17T12:00:00"}
    response = app_client.post("/save_result", json=mock_data)
    assert response.status_code == 200
    assert response.json["status"] == "success"
    mock_insert_one.assert_called_once_with(mock_data)


@mock.patch("app.collection.insert_one")
def test_save_result_no_data(mock_insert_one, app_client):
    """Test saving a classification result with no data."""
    response = app_client.post("/save_result", json={})
    assert response.status_code == 400
    assert response.json["status"] == "error"
    assert "No data received" in response.json["message"]
    mock_insert_one.assert_not_called()


@mock.patch("app.collection.find")
def test_results_route(mock_find, app_client):
    """Test the results route."""
    mock_find.return_value = [
        {"_id": "1", "classification": "clapping", "timestamp": "2024-11-17T12:00:00"}
    ]
    response = app_client.get("/results")
    assert response.status_code == 200
    assert b"Classification Result" in response.data


@mock.patch("app.collection.delete_one")
@mock.patch("app.ObjectId")
def test_delete_result(mock_object_id, mock_delete_one, app_client):
    """Test deleting a classification result."""
    result_id = "507f1f77bcf86cd799439011"  # Valid MongoDB ObjectId
    mock_object_id.return_value = result_id  # Mock ObjectId to avoid validation issues

    response = app_client.post(f"/delete_result/{result_id}")
    assert response.status_code == 302  # Redirects to /results
    mock_object_id.assert_called_once_with(result_id)
    mock_delete_one.assert_called_once_with({"_id": result_id})
