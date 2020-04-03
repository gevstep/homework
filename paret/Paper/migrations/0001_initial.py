# Generated by Django 3.0.4 on 2020-03-31 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_date', models.DateTimeField()),
                ('user_name', models.CharField(max_length=150)),
                ('exit_time', models.CharField(max_length=10)),
                ('exit_address', models.CharField(max_length=150)),
                ('visit_address', models.CharField(max_length=150)),
                ('visit_purpose', models.CharField(max_length=100)),
                ('return_time', models.CharField(max_length=10)),
            ],
        ),
    ]