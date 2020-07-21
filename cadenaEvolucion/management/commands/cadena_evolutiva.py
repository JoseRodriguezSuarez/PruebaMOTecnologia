from cadenaEvolucion.models import Pokemon
from django.core.management import BaseCommand
import requests, json, argparse






class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('id',type=int)

    
    def handle(self, *args, **kwargs):


        id_cadena_pok = kwargs['id']
        id_s = Pokemon.objects.filter(cadEvolutiva=id_cadena_pok)
        resultado_busqueda ={}
        data_total={}
        evolucion_list=[]
        data_total=[]
        url ='https://pokeapi.co/api/v2/evolution-chain/%s' % (id_cadena_pok)
        response = requests.get(url)
        resultado_busqueda = response.json()
        url1 =url_pokemon_1(resultado_busqueda)
        evolucion_list = evoluciones(resultado_busqueda["chain"]["evolves_to"])
        #se agrega el url del primer pokemon en el indice 0, del listado de urls a consultar
        #la coleccion es toda la cadena evolutiva
        evolucion_list.insert(0 ,[url1,1])
        #Ejecucion de las consultas, y creacion del diccionario final por pokemon, y la lista de todos los resultados
        
        for element in evolucion_list:
            url = element[0]
            id = buscar_id(url)
            data = buscar_pokemon_data(id)
            est= data[1]
            #Si la cadena evolutiva ya existe no la guarda pero aun asi muestra la consulta, esto para no saturar la db
            #y cuando se ejecute el servicio de consulta no recibir registros multiplicados
            if is_empty(id_s)==True:
                pok= Pokemon(nPok=data[4],nombre=data[0],peso=data[3], altura=data[2], cadEvolutiva=id_cadena_pok, hp=est[0], attack=est[1], defense=est[2], special_attack=est[3], special_defense=est[4], speed=est[5], nivelEvolutivo=element[1])
                pok.save()
            #Alistamiento de la data para ser mostrada en consola de manera amigable
            labels=["Nombre","Estadisticas","Altura","Peso","Id"]
            labelsSt=["hp","attack","defense","special_attack","special_defense","speed"]
            dictD = dict (zip(labelsSt,est))
            data[1]=dictD
            dictT = dict (zip(labels,data))
            data_total.append(dictT) 
        for data in data_total: 
            print (data)

        print("Cadena Evolutiva #: ", id_cadena_pok)
       


#Consulta si una estructua esta vacia    
def is_empty(data_structure):
    if data_structure:
        return False
    else:
        return True
#Busqueda de los links del metodo pokemon-species de todos los pokemons que integran la cadena evolutiva 
#menos el inicial ya que esta por fuera de la lista parametro de esta funcion
#se consulta en cada nivel de evolucion si existen mas como el caso de Eevee
#es extensible hasta el 3er nivel evolutivo aunque no conozco casos que un pokemon de nivel evolutivo tenga opciones a un 3er nivel
#a cada nivel evolutivo se le asigan un id ejem eevee=1 todas sus evoluciones son level 2, para lograr determinar
#el tipo de evolucion (preevolucion/evolucion)
def evoluciones(lista_evoluciones):
    evol=[]
    flag = is_empty(lista_evoluciones)
    if flag == False:
        x = 0
        longs=len(lista_evoluciones)
        while x < longs:
            url=lista_evoluciones[x]["species"]["url"]
            lista_evoluciones2=lista_evoluciones[x]["evolves_to"]
            flag=is_empty(lista_evoluciones2)
            if flag == False:
                y = 0
                longs2=len(lista_evoluciones2)
                while y  < longs2:
                    url2=lista_evoluciones2[y]["species"]["url"]
                    evol.append([url2,3])
                    y += 1
            evol.append([url,2])
            x += 1
    return evol

#Se extrae el url del primer pokemon de la cadena
def url_pokemon_1(dict):
    url_pokemon_primer=dict["chain"]["species"]["url"]
    return url_pokemon_primer

#Ejecuta el metodo de pokemon-Species para consultar el id del pokemon
def buscar_id(url):
    resultado_busqueda ={}
    response = requests.get(url)
    resultado_busqueda = response.json()
    id = resultado_busqueda["id"]
    return id

#Ejecuta el metodo Pokemon, para la consulta de la data requerida
def buscar_pokemon_data(id):
    resultado_busqueda ={}
    data=[]
    url ='https://pokeapi.co/api/v2/pokemon/%s'% (id)
    response = requests.get(url)
    resultado_busqueda = response.json()
    nombre=resultado_busqueda["name"]
    data.append(nombre)
    estadisticas=resultado_busqueda["stats"]
    estadisticas=pulir_estadisticas(estadisticas)
    data.append(estadisticas)
    altura=resultado_busqueda["height"]
    data.append(altura)
    peso=resultado_busqueda["weight"]
    data.append(peso)
    id = resultado_busqueda["id"]
    data.append(id)
    return data

#Extrae la informacion necesaria del listado de estadisticas y las organiza en un diccionario
def pulir_estadisticas(lista_estadisticas):
    idstats=[]
    x=0
    longs=len(lista_estadisticas)
    while x<longs:
            statsiq = lista_estadisticas[x]["base_stat"]
            idstats.append(statsiq)
            x += 1
    return idstats