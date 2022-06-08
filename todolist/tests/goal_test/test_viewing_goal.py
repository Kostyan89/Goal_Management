import pytest

from goals.serializers import GoalSerializer


@pytest.mark.django_db
def test_viewing_goal(client, logged_in_user,  goal):
    expected_response = GoalSerializer(goal).data

    response = client.get(f"/goals/goal/{goal.id}")

    assert response.status_code == 200
    assert response.json() == expected_response
