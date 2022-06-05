import freezegun
import pytest

from goals.models import GoalComment
from goals.serializers import CommentSerializer

@freezegun.freeze_time("2022-05-30")
@pytest.mark.django_db
def test_list_comment(client, logged_in_user, board, board_participants, board2_participants, goal):
    comment_1 = GoalComment.objects.create(text="test", goal=goal)
    comment_2 = GoalComment.objects.create(text="test", goal=goal)

    expected_response = [
        CommentSerializer(comment_1).data,
        CommentSerializer(comment_2).data,
    ]
    response = client.get("/goals/goal_comment/list")

    assert response.status_code == 200
    assert sorted(response.json(), key=lambda x: x['id']) == expected_response
