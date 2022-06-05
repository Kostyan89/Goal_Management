import pytest


@pytest.mark.django_db
def test_creating_board_authorized(client, logged_in_user):
    response = client.post(
        "/goals/board/create",
        {"title": "test"},
        content_type="application/json"
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_creating_unauthorized(client, board, board_participants):
    response = client.post(
        "/goals/board/create/",
        {"title": "test"},
        content_type="application/json"
    )

    assert response.status_code == 404
