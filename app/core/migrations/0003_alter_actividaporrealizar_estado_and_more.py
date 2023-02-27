# Generated by Django 4.1.7 on 2023-02-27 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_actividaporrealizar_usuario_asig_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividaporrealizar',
            name='estado',
            field=models.IntegerField(choices=[(1, 'Asignado'), (2, 'En Proceso'), (3, 'Terminado')], default=1),
        ),
        migrations.AlterField(
            model_name='actividaporrealizar',
            name='prioridad',
            field=models.IntegerField(choices=[(1, 'Alta'), (2, 'Media'), (3, 'Baja')], default=1),
        ),
    ]