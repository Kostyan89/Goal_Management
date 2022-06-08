import pytest


@pytest.mark.django_db
def test_deleting_goal(client, logged_in_user,  goal):

    response = client.delete(f"/goals/goal/{goal.id}")
    assert response.status_code == 204
