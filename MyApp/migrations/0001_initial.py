# Generated by Django 4.0.5 on 2022-06-30 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('mob', models.CharField(max_length=12)),
                ('subject', models.CharField(max_length=122)),
                ('msg', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
