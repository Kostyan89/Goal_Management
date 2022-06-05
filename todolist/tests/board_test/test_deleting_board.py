import pytest


@pytest.mark.django_db
def test_deleting_board(client, logged_in_user, board, board_participants):
    response = client.delete(f"/goals/board/{board.id}")
    assert response.status_code == 204

    response = client.get(f"/goals/board/{board.id}")
    assert response.status_code == 404
