# Generated by Django 5.1.5 on 2025-02-04 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Refrigerator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField()),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity_unit', models.CharField(choices=[('u', 'Units'), ('g', 'Grams'), ('mg', 'Milligrams'), ('kg', 'Killograms'), ('l', 'Liter'), ('cl', 'Centiliter'), ('ml', 'Milliliter')])),
            ],
            options={
                'unique_together': {('name', 'quantity', 'quantity_unit')},
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('expirationDate', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_nevera_api.food')),
                ('refrigerator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_nevera_api.refrigerator')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('mail', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('username', models.CharField()),
                ('bio', models.TextField()),
                ('avatar', models.ImageField(upload_to='')),
                ('refrigerator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_nevera_api.refrigerator')),
            ],
        ),
    ]
