# Generated by Django 4.0.3 on 2022-03-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.IntegerField(choices=[(0, 'Cancelled'), (-1, 'Pending for admin approval'), (1, 'Request accepted')], default=-1),
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
