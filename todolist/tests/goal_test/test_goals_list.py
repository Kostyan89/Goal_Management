
import pytest

from goals.models import Goal
from goals.serializers import GoalSerializer


@pytest.mark.django_db
def test_list_goals(client, logged_in_user, board, board2, board_participants, board2_participants, category):
    goal = Goal.objects.create(title="test", category=category, due_date="2022-06-05", user=logged_in_user)
    goal_2 = Goal.objects.create(title="test2", category=category, due_date="2022-06-05", user=logged_in_user)
    expected_response = [
        GoalSerializer(goal).data,
        GoalSerializer(goal_2).data,
    ]
    response = client.get("/goals/goal/list")

    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db
def test_list_goals_unauthorized(client, board, board2, board_participants, board2_participants, category):

    response = client.get("/goals/goal/list")

    assert response.status_code == 403
