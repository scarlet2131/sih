# Generated by Django 3.0.2 on 2020-01-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20200115_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm_details',
            name='img_crop',
            field=models.CharField(default='default', max_length=150),
            preserve_default=False,
        ),
    ]
