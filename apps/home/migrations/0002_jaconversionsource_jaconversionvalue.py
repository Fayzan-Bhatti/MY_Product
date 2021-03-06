# Generated by Django 3.2.6 on 2022-03-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JaConversionSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ja_conversion_source',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JaConversionValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cs_id', models.IntegerField()),
                ('project_management_id', models.IntegerField()),
                ('date', models.DateField()),
                ('total_conversion', models.IntegerField()),
                ('conversion_value', models.FloatField()),
            ],
            options={
                'db_table': 'ja_conversion_value',
                'managed': False,
            },
        ),
    ]
