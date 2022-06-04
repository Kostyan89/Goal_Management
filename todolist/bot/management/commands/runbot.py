import os

from todolist import settings


from django.conf import settings
from django.core.management import BaseCommand

from bot.models import TgUser
from bot.tg.client import TgClient
from bot.tg.dc import Message
from goals.models import Goal


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tg_client = TgClient(settings.BOT_TOKEN)

    @staticmethod
    def _generate_verification_code():
        return os.urandom(12).hex()

    def handle_goal_list(self, msg: Message, tg_user: TgUser):
        resp_goals: list[str] = [
            f'#{goal.id}, {goal.title}'
            for goal in Goal.objects.filter(user_id=tg_user.user)
        ]
        self.tg_client.send_message(msg.chat.id, '\n'.join(resp_goals) or '[no goals found]')

    def handle_verified_user(self, msg: Message, tg_user: TgUser):
        if "/goals" in msg.text:
            self.handle_goal_list(msg=msg, tg_user=tg_user)
        else:
            self.tg_client.send_message(msg.chat.id, "[unknown command]")

    def handle_user_without_verification(self, msg: Message, tg_user: TgUser):
        code: str = self._generate_verification_code()
        tg_user.verification_code = code
        tg_user.save(update_fields=['verification_code'])
        self.tg_client.send_message(chat_id=msg.chat.id,
                                    text=f'[verification code] {code}')

    def handle_message(self, msg: Message):
        tg_user, created = TgUser.objects.get_or_create(
            chat_id=msg.chat.id,
            defaults={
                "username": msg.from_.username,
            },
        )
        if created:
            self.tg_client.send_message(msg.chat.id, "[Hello!]")
        elif not tg_user.user:
            self.handle_user_without_verification(msg=msg, tg_user=tg_user)
        else:
            self.handle_verified_user(msg=msg, tg_user=tg_user)

    def handle(self, *args, **kwargs):
        offset = 0
        while True:
            resp = self.tg_client.get_updates(offset=offset)
            for item in resp.result:
                offset = item.update_id + 1
                self.handle_message(item.message)
