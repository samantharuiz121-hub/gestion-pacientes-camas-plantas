from django.db import models

# Create your models here.

class Paciente(models.Model):
    #Se crea una clase llamada Paciente equivale a una tabla en el modelo
    cedula_pac = models.CharField(max_length=20, primary_key=True)
    nombre_pac = models.CharField(max_length=100)
    apellidos_pac = models.CharField(max_length=100)
    fecha_nac_pac = models.DateField()
    foto_pac = models.ImageField(upload_to='pacientes/', blank=True, null=True)

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return self.cedula_pac


class Planta(models.Model):
    numero_pln = models.IntegerField(primary_key=True)
    nombre_pln = models.CharField(max_length=100)

    class Meta:
        db_table = 'planta'

    def __str__(self):
        return str(self.numero_pln)


class Cama(models.Model):
    codigo_cam = models.IntegerField(primary_key=True)
    detalle_cam = models.CharField(max_length=200)
    fecha = models.DateField()
    numero_planta = models.ForeignKey(
        Planta,
        on_delete=models.CASCADE,
        db_column='numero_planta'
    )
    cedula_paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        db_column='cedula_paciente'
    )

    class Meta:
        db_table = 'cama'

    def __str__(self):
        return str(self.codigo_cam)
