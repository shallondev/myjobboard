# Generated by Django 4.2.7 on 2024-02-28 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0006_alter_application_cover_letter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='applicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='application',
            name='cover_letter',
            field=models.FileField(blank=True, default='txt.pdf', null=True, upload_to='pdfs/cover_letters'),
        ),
        migrations.AlterField(
            model_name='application',
            name='middle_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
