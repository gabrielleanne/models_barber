from django.db import models

# Create your models here.



class Tb_usuario (models.Model):
    uso_codigo =models.IntegerField(primary_key=True)
    usu_email=models.CharField(max_length=100,)
    usu_senha=models.CharField(max_length=15,)



class Tb_agendamento (models.Model):
    age_codigo= models.IntegerField(primary_key=True)
    age_nome= models.CharField(max_length=45,)
    age_servico= models.CharField(max_length=45,)
    age_telefone=models.CharField(max_length=45,)
    age_ser_codigo=models.IntegerField()
    age_uso_codigo=models.IntegerField()




class Tb_TelefoneDoAgendamento (models.Model):
    tel_codigo=models.IntegerField(primary_key=True)
    tel_age_codigo= models.ForeignKey(Tb_agendamento, on_delete=models.CASCADE, default=None, null=True)


class Tb_servicos (models.Model):
    ser_codigo=models.IntegerField(primary_key=True)
    ser_servico=models.CharField(max_length=45)


