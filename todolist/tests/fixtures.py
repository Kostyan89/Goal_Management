import pytest

from bot.models import TgUser
from core.models import User
from goals.models import Board, BoardParticipant, GoalCategory, Goal, GoalComment

USERNAME = "john"
USER_PASSWORD = "123qwe"
USERNAME2 = "kostyan"
USER_PASSWORD2 = "123qwe2"


@pytest.fixture()
@pytest.mark.django_db
def user1(client, django_user_model):
    return django_user_model.objects.create_user(
        username=USERNAME,
        password=USER_PASSWORD
    )


@pytest.fixture()
@pytest.mark.django_db
def user2(client, django_user_model):
    return django_user_model.objects.create_user(
        username=USERNAME2,
        password=USER_PASSWORD2
    )


@pytest.fixture()
@pytest.mark.django_db
def logged_in_user(client, user1):
    client.login(username=USERNAME, password=USER_PASSWORD)
    return user1


@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test_user")


@pytest.fixture()
@pytest.mark.django_db
def board(client):
    return Board.objects.create(title="test")


@pytest.fixture()
@pytest.mark.django_db
def board2(client):
    return Board.objects.create(title="test2")


@pytest.fixture()
@pytest.mark.django_db
def board_participants(client, board, user1):
    return BoardParticipant.objects.create(board=board, user=user1)


@pytest.fixture()
@pytest.mark.django_db
def board2_participants(client, board2, user1):
    return BoardParticipant.objects.create(board=board2, user=user1)


@pytest.fixture()
@pytest.mark.django_db
def category(client, user1, board, board_participants):
    return GoalCategory.objects.create(title="test", user=user1, board=board)


@pytest.fixture()
@pytest.mark.django_db
def goal(client, category, logged_in_user):
    return Goal.objects.create(title="test", category=category, due_date="2022-06-05", user=logged_in_user)


@pytest.fixture()
@pytest.mark.django_db
def category_user1(client,category, user1, board):
    return GoalCategory.objects.create(title="test", user=user1, board=board)


@pytest.fixture()
@pytest.mark.django_db
def logged_in_user1(client, user2):
    client.login(username="test", password="test")
    return user2


@pytest.fixture()
@pytest.mark.django_db
def comment(client, goal):
    return GoalComment.objects.create(text="test", goal=goal)


@pytest.fixture()
@pytest.mark.django_db
def goal_user2(client, category, user2):
    return Goal.objects.create(title="test", category=category, due_date="2022-06-05", user=user2)


@pytest.fixture()
@pytest.mark.django_db
def verification_code(client, logged_in_user):
    return TgUser.objects.update(verification_code="0cfe170d9d76ca02eb59669e")
