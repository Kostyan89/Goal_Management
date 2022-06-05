import pytest

from goals.serializers import BoardSerializer


@pytest.mark.django_db
def test_viewing_board(client, logged_in_user, board, board_participants):
    expected_response = BoardSerializer(board).data

    response = client.get(f"/goals/board/{board.id}")

    assert response.status_code == 200
    assert response.json() == expected_response
