# Generated by Django 4.1.3 on 2022-11-29 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_topics',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=50)),
                ('topic_desc', models.CharField(max_length=200)),
                ('topic_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_name', models.CharField(max_length=50)),
                ('comment_desc', models.CharField(max_length=200)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topiccomment.tbl_topics')),
            ],
        ),
    ]
