# Generated by Django 3.2 on 2021-07-20 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_alter_comments_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.profile'),
        ),
        migrations.AlterField(
            model_name='community',
            name='c_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.profile'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='followed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to='community.profile'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='community.profile'),
        ),
        migrations.AlterField(
            model_name='like',
            name='like_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='upload_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.profile'),
        ),
    ]