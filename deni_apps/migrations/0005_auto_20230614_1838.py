# Generated by Django 3.2.16 on 2023-06-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deni_apps', '0004_auto_20230614_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatedetails',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='candidatedetails',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='candidatedetails',
            name='candiate_doj',
            field=models.DateField(default=None, verbose_name='Candidate Joining Date'),
        ),
    ]
