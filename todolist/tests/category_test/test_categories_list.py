import pytest

from goals.models import GoalCategory
from goals.serializers import GoalCategorySerializer


@pytest.mark.django_db
def test_list_category(client, logged_in_user, board, board_participants, board2_participants):
    category_1 = GoalCategory.objects.create(title="test", user=logged_in_user, board=board)
    category_2 = GoalCategory.objects.create(title="test2", user=logged_in_user, board=board)

    expected_response = [
        GoalCategorySerializer(category_1).data,
        GoalCategorySerializer(category_2).data,
    ]
    response = client.get("/goals/goal_category/list")

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_list_category_unauthorized(client, board, board_participants, board2_participants):

    response = client.get("/goals/goal_category/list")

    assert response.status_code == 403

