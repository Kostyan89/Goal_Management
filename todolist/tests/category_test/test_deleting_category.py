import pytest

from goals.models import GoalCategory


@pytest.mark.django_db
def test_deleting_category(client, board, logged_in_user):
    category = GoalCategory.objects.create(title="test", board=board, user= logged_in_user)
    response = client.delete(f"/goals/goal_category/{category.id}")

    assert response.status_code == 404
