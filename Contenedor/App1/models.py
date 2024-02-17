from django.db import models

class Profesion(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=75)
    
    def __str__(self) -> str:
        return self.nombre

# Create your models here.
class AutorDb(models.Model):
    
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    fecha_nacimiento = models.DateField(verbose_name="Fecha nacimiento", null="false", blank=False)
    fecha_fallecimiento = models.DateField(verbose_name="Fecha fallecimiento", null=True, blank="True")
    profesion = models.ManyToManyField(Profesion, verbose_name="Profesion")
    nacionalidad = models.CharField(verbose_name="Nacionalidad", max_length=50)
    
    class Meta:
        db_table = "Autores"
        verbose_name= "Autor"
        verbose_name_plural = "Autores"
        
    def __str__(self) -> str:
        return self.nombre
    
class FraseDb(models.Model):
    
    cita = models.TextField(verbose_name="Cita", max_length="400")
    autor_fk = models.ForeignKey(AutorDb, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name= "Frase"
        verbose_name_plural = "Frases"
    
