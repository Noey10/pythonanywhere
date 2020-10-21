# Generated by Django 2.2.7 on 2020-10-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0002_auto_20201017_0622'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=255)),
                ('Lastname', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('status', models.BooleanField(blank=True, default='False')),
            ],
        ),
        migrations.AddField(
            model_name='cactus',
            name='img',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='cactus',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
