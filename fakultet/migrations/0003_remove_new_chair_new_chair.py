# Generated by Django 4.2.1 on 2023-07-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakultet', '0002_faculty_sub_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='chair',
        ),
        migrations.AddField(
            model_name='new',
            name='chair',
            field=models.ManyToManyField(blank=True, to='fakultet.chair', verbose_name='Kafedra news'),
        ),
    ]
