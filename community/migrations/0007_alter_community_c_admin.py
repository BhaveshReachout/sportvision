# Generated by Django 3.2 on 2021-07-23 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_alter_post_upload_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='c_admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.profile'),
        ),
    ]
