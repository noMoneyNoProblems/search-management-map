# Generated by Django 3.0.6 on 2020-05-23 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0016_migrate_polygontimelabel'),
        ('search', '0014_auto_20200523_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linestringtimelabel',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='linestringtimelabel',
            name='gtl',
        ),
        migrations.RemoveField(
            model_name='linestringtimelabel',
            name='mission',
        ),
        migrations.RemoveField(
            model_name='linestringtimelabel',
            name='replaced_by',
        ),
        migrations.RemoveField(
            model_name='pointtimelabel',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='pointtimelabel',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='pointtimelabel',
            name='gtl',
        ),
        migrations.RemoveField(
            model_name='pointtimelabel',
            name='mission',
        ),
        migrations.RemoveField(
            model_name='pointtimelabel',
            name='replaced_by',
        ),
        migrations.RemoveField(
            model_name='polygontimelabel',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='polygontimelabel',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='polygontimelabel',
            name='gtl',
        ),
        migrations.RemoveField(
            model_name='polygontimelabel',
            name='mission',
        ),
        migrations.RemoveField(
            model_name='polygontimelabel',
            name='replaced_by',
        ),
    ]