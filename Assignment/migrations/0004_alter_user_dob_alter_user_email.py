# Generated by Django 4.0.5 on 2022-06-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment', '0003_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=300, unique=True),
        ),
    ]