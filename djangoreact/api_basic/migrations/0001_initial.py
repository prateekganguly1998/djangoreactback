# Generated by Django 3.1.4 on 2020-12-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('difficulty', models.CharField(default='EASY', max_length=20)),
                ('question', models.TextField()),
                ('options', models.JSONField()),
                ('answer', models.TextField()),
            ],
        ),
    ]
