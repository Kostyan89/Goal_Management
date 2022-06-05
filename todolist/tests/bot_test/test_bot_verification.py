import pytest

from bot.serializers import TgUserSerializer


@pytest.mark.django_db
def test_bot_verification(client, logged_in_user, verification_code):
    expected_response = TgUserSerializer(verification_code).data
    expected_response["verification_code"] = "0cfe170d9d76ca02eb59669e"
    response = client.patch(
        f"/goals/bot/verify",
        {"verification_code": "0cfe170d9d76ca02eb59669e"},
        content_type="application/json"
    )

    assert response.status_code == 200
