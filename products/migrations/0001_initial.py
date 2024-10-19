# Generated by Django 5.1.2 on 2024-10-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.TextField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('internalReference', models.CharField(max_length=250)),
                ('shellId', models.CharField(max_length=100)),
                ('inventoryStatus', models.CharField(choices=[('INSTOCK', 'Instock'), ('LOWSTOCK', 'Lowstock'), ('OUTOFSTOCK', 'Outofstock')], default='INSTOCK', max_length=50)),
                ('rating', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
