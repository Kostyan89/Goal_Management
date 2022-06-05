import pytest


from goals.serializers import BoardListSerializer


@pytest.mark.django_db
def test_boards_list(client, logged_in_user, board, board2, board_participants, board2_participants):
    expected_response = [
        BoardListSerializer(board).data,
        BoardListSerializer(board2).data,
    ]
    response = client.get("/goals/board/list")

    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db
def test_boards_list(client, board, board2, board_participants, board2_participants):

    response = client.get("/goals/board/list")

    assert response.status_code == 403

