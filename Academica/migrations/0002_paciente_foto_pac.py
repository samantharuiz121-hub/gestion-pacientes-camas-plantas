# Generated for adding a patient photo.
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='foto_pac',
            field=models.ImageField(blank=True, null=True, upload_to='pacientes/'),
        ),
    ]
