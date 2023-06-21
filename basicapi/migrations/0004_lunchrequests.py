# Generated by Django 4.0.2 on 2023-06-21 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicapi', '0003_user_chatwork_id_alter_user_kaonavi_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LunchRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_calender_uid', models.CharField(max_length=255)),
                ('apply_content', models.CharField(max_length=255)),
                ('preferred_days', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
