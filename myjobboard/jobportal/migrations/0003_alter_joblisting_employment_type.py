# Generated by Django 4.2.7 on 2024-02-24 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0002_rename_description_joblisting_summary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='employment_type',
            field=models.CharField(default='full-time', max_length=100),
            preserve_default=False,
        ),
    ]