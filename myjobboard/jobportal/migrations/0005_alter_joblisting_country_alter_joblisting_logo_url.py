# Generated by Django 4.2.7 on 2024-02-25 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0004_alter_joblisting_bonus_skills_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='country',
            field=models.CharField(default='Canada', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='logo_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]