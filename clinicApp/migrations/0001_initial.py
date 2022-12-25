# Generated by Django 4.1.3 on 2022-12-25 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HojaAtencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut_Paciente', models.CharField(max_length=25)),
                ('Profesional_que_Atendio', models.CharField(max_length=25)),
                ('Fecha_Atencion', models.DateTimeField(blank=True, null=True)),
                ('Alergias', models.CharField(max_length=125)),
                ('Historial_de_Enfermedades', models.CharField(max_length=500)),
                ('Medicamentos_que_toma', models.CharField(max_length=250)),
                ('Anamnesis', models.TextField(max_length=250)),
                ('Diagnostico', models.TextField(max_length=500)),
                ('Medicamentos_Recetados', models.CharField(max_length=250)),
                ('Examenes_Solicitados', models.CharField(max_length=250)),
                ('Observaciones', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut', models.CharField(max_length=12)),
                ('Nombres', models.CharField(max_length=50)),
                ('Apellido_Paterno', models.CharField(max_length=25)),
                ('Apellido_Materno', models.CharField(max_length=25)),
                ('Fecha_Nacimiento', models.DateTimeField(blank=True, null=True)),
                ('Genero', models.CharField(max_length=25)),
                ('Direccion', models.CharField(max_length=25)),
                ('Comuna', models.CharField(max_length=25)),
                ('Nacionalidad', models.CharField(max_length=25)),
                ('Telefono', models.CharField(max_length=25)),
                ('Contacto_de_Emergencia', models.CharField(max_length=25)),
                ('Telefono_de_Emergencia', models.CharField(max_length=25)),
                ('Sistema_de_Salud', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut', models.CharField(max_length=12)),
                ('Nombres', models.CharField(max_length=50)),
                ('Apellido_Paterno', models.CharField(max_length=25, verbose_name='Apellido Paterno')),
                ('Apellido_Materno', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut', models.CharField(max_length=12)),
                ('Nombres', models.CharField(max_length=50)),
                ('Apellido_Paterno', models.CharField(max_length=25)),
                ('Apellido_Materno', models.CharField(max_length=25)),
                ('Categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinicApp.especialidades')),
            ],
        ),
    ]
