# Generated by Django 5.1.1 on 2024-09-22 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_ticker_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
