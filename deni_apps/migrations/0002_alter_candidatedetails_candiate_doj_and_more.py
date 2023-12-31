# Generated by Django 4.2.2 on 2023-06-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deni_apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatedetails',
            name='candiate_doj',
            field=models.DateField(verbose_name='Candidate Joining Date'),
        ),
        migrations.AlterField(
            model_name='candidatedetails',
            name='candiate_email_id',
            field=models.EmailField(max_length=50, verbose_name='Candidate Email Id'),
        ),
        migrations.AlterField(
            model_name='candidatedetails',
            name='hiring_manager',
            field=models.CharField(max_length=100, verbose_name='Hiring Manager'),
        ),
        migrations.AlterField(
            model_name='candidatedetails',
            name='hiring_manager_email_id',
            field=models.EmailField(max_length=50, verbose_name='Hiring Manager Email Id'),
        ),
        migrations.AlterField(
            model_name='candidatedetails',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
