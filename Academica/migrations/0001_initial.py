# Generated for the PACIENTE, CAMA and PLANTA tables in the UML.
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cedula_pac', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre_pac', models.CharField(max_length=100)),
                ('apellidos_pac', models.CharField(max_length=100)),
                ('fecha_nac_pac', models.DateField()),
            ],
            options={'db_table': 'paciente'},
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('numero_pln', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_pln', models.CharField(max_length=100)),
            ],
            options={'db_table': 'planta'},
        ),
        migrations.CreateModel(
            name='Cama',
            fields=[
                ('codigo_cam', models.IntegerField(primary_key=True, serialize=False)),
                ('detalle_cam', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('numero_planta', models.ForeignKey(db_column='numero_planta', on_delete=django.db.models.deletion.CASCADE, to='Academica.planta')),
                ('cedula_paciente', models.ForeignKey(db_column='cedula_paciente', on_delete=django.db.models.deletion.CASCADE, to='Academica.paciente')),
            ],
            options={'db_table': 'cama'},
        ),
    ]
