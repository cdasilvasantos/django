# Generated by Django 4.2.6 on 2023-11-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='todoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('this_item', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
