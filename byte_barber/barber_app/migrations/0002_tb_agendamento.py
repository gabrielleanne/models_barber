# Generated by Django 4.2.5 on 2023-09-28 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tb_agendamento',
            fields=[
                ('age_codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('age_nome', models.CharField(max_length=45)),
                ('age_servico', models.CharField(max_length=45)),
                ('age_telefone', models.CharField(max_length=45)),
                ('age_ser_codigo', models.IntegerField()),
                ('age_uso_codigo', models.IntegerField()),
            ],
        ),
    ]