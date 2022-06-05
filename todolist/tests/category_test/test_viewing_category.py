
import pytest

from goals.serializers import GoalCategorySerializer


@pytest.mark.django_db
def test_viewing_category(client, logged_in_user, category):
    category = category
    expected_response = GoalCategorySerializer(category).data

    response = client.get(f"/goals/goal_category/{category.id}")

    assert response.status_code == 200
    assert response.json() == expected_response
