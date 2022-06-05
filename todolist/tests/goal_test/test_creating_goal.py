
import pytest


@pytest.mark.django_db
def test_creating_goal(client, logged_in_user, category):

    response = client.post(
        "/goals/goal/create",
        {
            "title": "title",
            "category": category.id,
            "due_date": "2022-06-05"
        },
        content_type="application/json"
    )

    assert response.status_code == 201
