# Generated by Django 5.0.3 on 2024-03-05 09:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_category_active_category_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]