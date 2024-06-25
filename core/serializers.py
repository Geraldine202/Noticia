from rest_framework import serializers
from .models import *

#Lo utilizamos para poder transformar python a json
class categoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields ='__all__'


class periodistaSerializers(serializers.ModelSerializer):
    especialidad = categoriaSerializers(read_only=True)
    class Meta:
        model= Periodista
        fields ='__all__'

class noticiaSerializers(serializers.ModelSerializer):
    tipo = categoriaSerializers(read_only=True)
    nombre_periodista = periodistaSerializers(read_only=True)
    class Meta:
        model= Noticia
        fields ='__all__'