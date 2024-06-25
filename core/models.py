from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.descripcion
    

class Periodista(models.Model):
    nombre_completo= models.CharField(max_length=150)
    rut = models.CharField(max_length=12)
    edad = models.IntegerField(default=0)
    genero = models.CharField(max_length=10, choices=[('masculino','Masculino'),('femenino','Femenino')], default='masculino')
    telefono = models.CharField(max_length=14)
    especialidad= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = CloudinaryField('imagen')
    habilitado = models.BooleanField(default=True)


    def __str__(self):
        return self.nombre_completo
  

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.CharField(max_length=5000)
    fecha = models.DateField()
    ciudad = models.CharField(max_length=50)
    imagen = CloudinaryField('imagen')
    nombre_periodista = models.ForeignKey(Periodista, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Categoria, on_delete=models.CASCADE) #CASCADE o PROTECTED#
    estado = models.CharField(max_length=10, choices=[('pendiente','Pendiente'),('aprobado','Aprobado'),('rechazado','Rechazado')], default='pendiente')
    comentario = models.CharField(max_length=5000,blank=True,null=True)
    

    def __str__(self):
        return self.titulo
    



