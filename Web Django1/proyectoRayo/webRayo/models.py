from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre=models.CharField(primary_key=True,max_length=45)
    
    def __str__(self) -> str:
        return super().__str__()
    
        
        
class Vehiculo(models.Model):
    patente=models.TextField(primary_key=True)
    nombre_modelo=models.CharField(max_length=45)
    marca=models.CharField(max_length=45)
    año=models.IntegerField()
    descripcion=models.TextField()
    foto=models.ImageField(upload_to='fotos')
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre
        