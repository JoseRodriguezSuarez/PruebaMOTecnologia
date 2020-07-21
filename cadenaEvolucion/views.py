from django.http import HttpResponse
from .models import Pokemon
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializer import PokemonSerializer


# Create your views here.


class JSONResponse(HttpResponse):
    def __inti__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse, self).__init__(content,**kwargs)


def serie_list(request):
    pok_1 = Pokemon.objects.all()
    serializer = PokemonSerializer(pok_1, many=True)
    return JSONResponse(serializer.data)

def serie_pok(request, nombre):
    res=[]
    typeEvol=""
    pok_1 = Pokemon.objects.get(nombre=nombre)
    niv=pok_1.nivelEvolutivo
    #print(niv)
    pok_2 = Pokemon.objects.filter(cadEvolutiva=pok_1.cadEvolutiva)
    for pok in pok_2:
        print (pok.nivelEvolutivo)
        if niv > pok.nivelEvolutivo:
            typeEvol="Pre Evolucion"
            res.append([pok, typeEvol])
        elif niv < pok.nivelEvolutivo:
            typeEvol="Evolucion"
            res.append([pok , typeEvol])
        elif niv == pok.nivelEvolutivo:
            typeEvol="mismo nivel o pokemon seleccionado"
            res.append([pok, typeEvol])
    print(res)
    serializer = PokemonSerializer(pok_2, many=True)
    return JSONResponse(serializer.data)