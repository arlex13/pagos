# Generated by Django 4.0.6 on 2022-08-10 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='tipo',
            field=models.IntegerField(choices=[(10, 'Servicio Agua'), (20, 'Servicio Cementerio')], default=10),
        ),
    ]