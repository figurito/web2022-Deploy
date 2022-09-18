from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    slug= models.SlugField()

    class Meta:
        ordering =('nombre',)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria= models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    slug= models.SlugField()
    descripcion = models.TextField(blank=True, null=True)
    precio= models.IntegerField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('-fechaCreacion',)

    def __str__(self):
        return self.nombre

