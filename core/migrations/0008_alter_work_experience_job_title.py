# Generated by Django 4.2.5 on 2023-09-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_work_experience_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_experience',
            name='job_title',
            field=models.CharField(max_length=50),
        ),
    ]