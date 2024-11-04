# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Alumnos(models.Model):
    alumno_id = models.BigAutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=50)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    codigo_alumno = models.CharField(max_length=8)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=50)
    sexo = models.CharField(max_length=12)
    carrera = models.ForeignKey('Carreras', models.DO_NOTHING)
    correo_estudiantil = models.CharField(max_length=60, null=True)

    class Meta:
        managed = False
        db_table = 'alumnos'


class Carreras(models.Model):
    carrera_id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    numero_ciclos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'carreras'


class Cursos(models.Model):
    cursos_id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    horario = models.TimeField()
    cantidad_horas = models.IntegerField()
    numero_creditos = models.IntegerField()
    carrera = models.ForeignKey(Carreras, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cursos'


class Matriculas(models.Model):
    matricula_id = models.BigAutoField(primary_key=True)
    fecha_matricula = models.DateField()
    alumno = models.ForeignKey(Alumnos, models.DO_NOTHING)
    carrera = models.ForeignKey(Carreras, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'matriculas'


class Pagos(models.Model):
    pagos_id = models.BigAutoField(primary_key=True)
    monto = models.IntegerField()
    numero_cuota = models.IntegerField()
    fecha_pago = models.DateField()
    matricula = models.ForeignKey(Matriculas, models.DO_NOTHING)
    estado_pago = models.CharField(max_length=45,  null=True)

    class Meta:
        managed = False
        db_table = 'pagos'
