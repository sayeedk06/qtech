# Generated by Django 3.1.7 on 2021-04-02 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Search_history', '0002_auto_20210402_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchmodel',
            name='search_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='searchtimemodel',
            name='date',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Search_history.searchmodel'),
        ),
    ]
