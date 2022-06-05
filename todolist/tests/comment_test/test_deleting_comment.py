import pytest


@pytest.mark.django_db
def test_deleting_comment(client, logged_in_user,  comment):
    comment = comment

    response = client.delete(f"/goals/goal/{comment.id}")
    assert response.status_code == 204
