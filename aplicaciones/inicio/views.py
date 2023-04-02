from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio/index.html')

def listar_personas(request):
    lista_personas = {
        "titulo": 'Lista de personas',
        "personas": [{'nombre':'juan','edad':12}, {'nombre':'jose','edad':23}, {'nombre':'juan','edad':12}]
    }
    return render(request, "inicio/listar_personas.html",lista_personas)