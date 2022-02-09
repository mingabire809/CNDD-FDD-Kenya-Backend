# Generated by Django 3.2.6 on 2022-02-06 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecentActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='', verbose_name='picture')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('date', models.DateTimeField(verbose_name='Day of publication')),
            ],
        ),
    ]