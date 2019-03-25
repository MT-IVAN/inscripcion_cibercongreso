# Generated by Django 2.1.5 on 2019-03-21 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cupo', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('lugar', models.CharField(max_length=100)),
                ('ponente', models.CharField(max_length=100)),
                ('computador', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('identificacion', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombreCompleto', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('numCupon', models.CharField(max_length=6)),
                ('valor', models.CharField(max_length=9)),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='curso.Curso')),
            ],
        ),
    ]
