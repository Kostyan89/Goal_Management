import pytest

from core.models import User
from goals.serializers import CommentSerializer


@pytest.mark.django_db
def test_viewing_comment(client, logged_in_user, goal, comment):
    expected_response = CommentSerializer(comment).data

    response = client.get(f"/goals/goal_comment/{comment.id}")

    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db
def test_viewing_comment_unauthorized(client, comment2):

    response = client.get(f"/goals/goal_comment/{comment2.id}")

    assert response.status_code == 403
