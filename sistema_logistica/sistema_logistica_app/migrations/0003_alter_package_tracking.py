# Generated by Django 4.2.4 on 2023-08-10 16:30

from django.db import migrations, models
import sistema_logistica_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_logistica_app', '0002_rename_tipo_paquete_package_typepackage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='tracking',
            field=models.CharField(default=sistema_logistica_app.models.generateTracking, max_length=20, primary_key=True, serialize=False),
        ),
    ]
