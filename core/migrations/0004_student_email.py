# Generated by Django 4.2.7 on 2023-11-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_course_semester_alter_course_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
