# Generated by Django 4.0.6 on 2022-08-10 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_proyecto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='city',
            name='department',
        ),
        migrations.RemoveField(
            model_name='city',
            name='updatedBy',
        ),
        migrations.RemoveField(
            model_name='department',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='department',
            name='updatedBy',
        ),
        migrations.RemoveField(
            model_name='file',
            name='beneficiary',
        ),
        migrations.RemoveField(
            model_name='file',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='file',
            name='movement',
        ),
        migrations.RemoveField(
            model_name='file',
            name='updatedBy',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='beneficiary',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='project',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='sponsor',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='updatedBy',
        ),
        migrations.RemoveField(
            model_name='project',
            name='city',
        ),
        migrations.RemoveField(
            model_name='project',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='project',
            name='department',
        ),
        migrations.RemoveField(
            model_name='project',
            name='type',
        ),
        migrations.RemoveField(
            model_name='project',
            name='updatedBy',
        ),
        migrations.RemoveField(
            model_name='projectbeneficiary',
            name='beneficiary',
        ),
        migrations.RemoveField(
            model_name='projectbeneficiary',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='projectbeneficiary',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectbeneficiary',
            name='sponsor',
        ),
        migrations.RemoveField(
            model_name='projectbeneficiary',
            name='updatedBy',
        ),
        migrations.RemoveField(
            model_name='projecttypes',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='projecttypes',
            name='updatedBy',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='createdBy',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='updatedBy',
        ),
        migrations.DeleteModel(
            name='Beneficiary',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Movement',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectBeneficiary',
        ),
        migrations.DeleteModel(
            name='ProjectTypes',
        ),
        migrations.DeleteModel(
            name='Sponsor',
        ),
    ]