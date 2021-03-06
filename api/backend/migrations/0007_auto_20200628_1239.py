# Generated by Django 3.0.7 on 2020-06-28 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20200628_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('badge_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('icon', models.ImageField(upload_to='badge_icons/')),
                ('point_awarded', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='badges',
            field=models.ManyToManyField(blank=True, null=True, to='backend.Badge'),
        ),
    ]
