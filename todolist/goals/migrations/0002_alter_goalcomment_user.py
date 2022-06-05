# Generated by Django 4.0.3 on 2022-06-05 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalcomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]