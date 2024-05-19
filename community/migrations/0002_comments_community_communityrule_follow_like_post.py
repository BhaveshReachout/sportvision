# Generated by Django 3.2 on 2021-07-20 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('c_name', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('visiblity', models.CharField(choices=[('private', 'private'), ('public', 'public')], max_length=20)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc', models.CharField(max_length=20)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('c_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Community',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=25)),
                ('msg', models.TextField(max_length=500)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('upload_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Post',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('like_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('like_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.post')),
            ],
            options={
                'db_table': 'Like',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.profile')),
            ],
            options={
                'db_table': 'Follow',
            },
        ),
        migrations.CreateModel(
            name='CommunityRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=500)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community')),
            ],
            options={
                'db_table': 'CommunityRule',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(max_length=500)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('flag', models.CharField(blank=True, choices=[('racist', 'racist'), ('abbusing', 'abbusing')], max_length=20, null=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.post')),
            ],
            options={
                'db_table': 'Comments',
            },
        ),
    ]
