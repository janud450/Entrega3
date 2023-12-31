# Generated by Django 4.2.4 on 2023-08-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Garantia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=50)),
                ('contrato', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_inicial', models.DateTimeField()),
                ('fecha_final', models.DateTimeField()),
            ],
        ),
    ]
