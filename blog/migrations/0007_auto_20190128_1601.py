# Generated by Django 2.1.5 on 2019-01-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190128_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]
