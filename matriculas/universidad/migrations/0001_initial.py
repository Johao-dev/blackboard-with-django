# Generated by Django 5.1.2 on 2024-10-31 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('alumno_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=50)),
                ('codigo_alumno', models.CharField(max_length=8)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'alumnos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('carrera_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('numero_ciclos', models.IntegerField()),
            ],
            options={
                'db_table': 'carreras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('cursos_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('horario', models.TimeField()),
                ('cantidad_horas', models.IntegerField()),
                ('numero_creditos', models.IntegerField()),
            ],
            options={
                'db_table': 'cursos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Matriculas',
            fields=[
                ('matricula_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_matricula', models.DateField()),
            ],
            options={
                'db_table': 'matriculas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('pagos_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('numero_cuota', models.IntegerField()),
                ('fecha_pago', models.DateField()),
                ('estado_pago', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'pagos',
                'managed': False,
            },
        ),
    ]
