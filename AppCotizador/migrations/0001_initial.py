# Generated by Django 5.0.2 on 2024-03-07 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_material', models.CharField(max_length=20)),
                ('thickness', models.DecimalField(decimal_places=2, max_digits=4)),
                ('thick_tolerance_min', models.DecimalField(decimal_places=2, max_digits=2)),
                ('thick_tolerance_max', models.DecimalField(decimal_places=2, max_digits=2)),
                ('width', models.DecimalField(decimal_places=4, max_digits=7)),
                ('width_tolerance_min', models.DecimalField(decimal_places=2, max_digits=2)),
                ('width_tolerance_max', models.DecimalField(decimal_places=2, max_digits=2)),
                ('feed', models.DecimalField(decimal_places=4, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_type', models.CharField(max_length=20)),
                ('equipment', models.CharField(max_length=20)),
                ('pcs_stroke', models.IntegerField()),
                ('lots_per_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_date', models.DateField()),
                ('deadline', models.DateField()),
                ('customer', models.CharField(max_length=20)),
                ('part_number', models.CharField(max_length=30)),
                ('part_description', models.CharField(max_length=60)),
                ('platform', models.CharField(max_length=20)),
                ('annual_volume', models.IntegerField()),
                ('lifetime_years', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tooling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_tooling', models.CharField(max_length=20)),
                ('tooling_cost', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
