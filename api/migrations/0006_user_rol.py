# Generated by Django 4.0.6 on 2022-07-20 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_user_createdby_alter_user_updatedby_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='api.rol'),
        ),
    ]
