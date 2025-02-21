# Generated by Django 3.2.25 on 2024-09-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_homepage', models.BooleanField(default=False)),
                ('layout', models.CharField(choices=[('list', 'List'), ('gird', 'Grid')], max_length=10)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], max_length=10)),
                ('ordering', models.IntegerField(default=0)),
            ],
        ),
    ]
