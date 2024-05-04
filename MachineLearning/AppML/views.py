from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
import joblib
# Create your views here.

# MODEL - VIEW - TEMPLATE
# MVC: MODEL VIEW CONTROLER


modelo = joblib.load('modelo_entrenado_V4.pkl')

def es_analista(user):
    return user.groups.filter(name='analista').exists()


def home(request):
    #return HttpResponse("Home Page")
    return render(request, "home.html")

@login_required
def datos(request):

    return render(request, "datos.html")

@login_required
def prediccion(request):

    return render(request, "prediccion.html")



#REGISTRO LOGIN
@login_required
def logine(request):
    return render(request, "login.html")

def exit(request):
    logout(request)
    return render(request, "home.html")

def register(request):
    
    data = {
        "form": CustomUserCreationForm(),
    }
    
    if request.method == "POST":
        user_creation = CustomUserCreationForm(data = request.POST)
        if user_creation.is_valid():
            user_creation.save()
            user = authenticate(username = user_creation.cleaned_data['username'], password =  user_creation.cleaned_data['password1'])
            login(request, user)
            return redirect("home")
    return render(request, "registration/register.html", data)



def mostrar_formulario(request):
   # Inicializar la probabilidad en 0
    probabilidad_prediccion = 0
    
    if request.method == 'POST':
        # Obtener los datos del formulario
        datos_formulario = request.POST.dict()

        # Preparar los datos para la predicción
        datos_de_entrada = {
        'FLAG_SEXO_FEMENINO': int(datos_formulario.get('FLAG_SEXO_FEMENINO', 0)),
        'FLAG_SEXO_MASCULINO': int(datos_formulario.get('FLAG_SEXO_MASCULINO', 0)),
        'FLAG_TIENE_SEGURO': int(datos_formulario.get('FLAG_TIENE_SEGURO', 0)),
        'FLAG_SIN_SEGURO': int(datos_formulario.get('FLAG_SIN_SEGURO', 0)),
        'FLAG_RINOFARINGITIS_AGUDA_RINITIS': int(datos_formulario.get('FLAG_RINOFARINGITIS_AGUDA_RINITIS', 0)),
        'FLAG_CONSULTA_NUTRICIONAL_ATENCION_EN_NUTRICION': int(datos_formulario.get('FLAG_CONSULTA_NUTRICIONAL_ATENCION_EN_NUTRICION', 0)),
        'FLAG_RINITIS_ALERGICA': int(datos_formulario.get('FLAG_RINITIS_ALERGICA', 0)),
        'FLAG_INFECCION_VIAS_URINARIAS_SITIO_NO_ESPECIFICADO': int(datos_formulario.get('FLAG_INFECCION_VIAS_URINARIAS_SITIO_NO_ESPECIFICADO', 0)),
        'FLAG_EXAMEN_PESQUISA_ENFERMEDADES_SANGRE': int(datos_formulario.get('FLAG_EXAMEN_PESQUISA_ENFERMEDADES_SANGRE', 0)),
        'FLAG_ASMA_NO_ESPECIFICADA': int(datos_formulario.get('FLAG_ASMA_NO_ESPECIFICADA', 0)),
        'FLAG_PURPURA_TROMBOCITOPENICA_IDIOPATICA': int(datos_formulario.get('FLAG_PURPURA_TROMBOCITOPENICA_IDIOPATICA', 0)),
        'FLAG_ENFERMEDAD_RENAL_CRONICA_ETAPA_5': int(datos_formulario.get('FLAG_ENFERMEDAD_RENAL_CRONICA_ETAPA_5', 0)),
        'FLAG_ENFERMEDAD_RENAL_CRONICA': int(datos_formulario.get('FLAG_ENFERMEDAD_RENAL_CRONICA', 0)),
        'FLAG_PARASITOSIS_INTESTINAL': int(datos_formulario.get('FLAG_PARASITOSIS_INTESTINAL', 0)),
        'FLAG_EXAMEN_PESQUISA_TRASTORNOS_CARDIOVASCULARES': int(datos_formulario.get('FLAG_EXAMEN_PESQUISA_TRASTORNOS_CARDIOVASCULARES', 0)),
        'FLAG_ADMINISTRACION_DE_FACTOR_VIII_ENDOVENOSO': int(datos_formulario.get('FLAG_ADMINISTRACION_DE_FACTOR_VIII_ENDOVENOSO', 0)),
        'FLAG_DEFICIENCIA_HEREDITARIA_DEL_FACTOR_VIII': int(datos_formulario.get('FLAG_DEFICIENCIA_HEREDITARIA_DEL_FACTOR_VIII', 0)),
        'FLAG_NEUMONIA_NO_ESPECIFICADA': int(datos_formulario.get('FLAG_NEUMONIA_NO_ESPECIFICADA', 0)),
    }

        # Convertir el diccionario de entrada en una lista de listas
        datos_de_entrada_lista = [[valor for valor in datos_de_entrada.values()]]

        # Realizar la predicción de probabilidad
        probabilidades_prediccion = modelo.predict_proba(datos_de_entrada_lista)

        # Obtener la probabilidad de la clase positiva (1)
        probabilidad_clase_positiva = probabilidades_prediccion[0][1]

        # Convertir la probabilidad a porcentaje
        probabilidad_prediccion = probabilidad_clase_positiva * 100

    return render(request, 'formulario.html', {'probabilidad_prediccion': probabilidad_prediccion})


def realizar_prediccion(request):
     if request.method == 'POST':
        # Obtener los datos del formulario
        datos_de_entrada = {
            'FLAG_SEXO_FEMENINO': int(request.POST.get('FLAG_SEXO_FEMENINO', 0)),
            'FLAG_SEXO_MASCULINO': int(request.POST.get('FLAG_SEXO_MASCULINO', 0)),
            'FLAG_TIENE_SEGURO': int(request.POST.get('FLAG_TIENE_SEGURO', 0)),
            'FLAG_SIN_SEGURO': int(request.POST.get('FLAG_SIN_SEGURO', 0)),
            'FLAG_RINOFARINGITIS_AGUDA_RINITIS': int(request.POST.get('FLAG_RINOFARINGITIS_AGUDA_RINITIS', 0)),
            'FLAG_CONSULTA_NUTRICIONAL_ATENCION_EN_NUTRICION': int(request.POST.get('FLAG_CONSULTA_NUTRICIONAL_ATENCION_EN_NUTRICION', 0)),
            'FLAG_RINITIS_ALERGICA': int(request.POST.get('FLAG_RINITIS_ALERGICA', 0)),
            'FLAG_INFECCION_VIAS_URINARIAS_SITIO_NO_ESPECIFICADO': int(request.POST.get('FLAG_INFECCION_VIAS_URINARIAS_SITIO_NO_ESPECIFICADO', 0)),
            'FLAG_EXAMEN_PESQUISA_ENFERMEDADES_SANGRE': int(request.POST.get('FLAG_EXAMEN_PESQUISA_ENFERMEDADES_SANGRE', 0)),
            'FLAG_ASMA_NO_ESPECIFICADA': int(request.POST.get('FLAG_ASMA_NO_ESPECIFICADA', 0)),
            'FLAG_PURPURA_TROMBOCITOPENICA_IDIOPATICA': int(request.POST.get('FLAG_PURPURA_TROMBOCITOPENICA_IDIOPATICA', 0)),
            'FLAG_ENFERMEDAD_RENAL_CRONICA_ETAPA_5': int(request.POST.get('FLAG_ENFERMEDAD_RENAL_CRONICA_ETAPA_5', 0)),
            'FLAG_ENFERMEDAD_RENAL_CRONICA': int(request.POST.get('FLAG_ENFERMEDAD_RENAL_CRONICA', 0)),
            'FLAG_PARASITOSIS_INTESTINAL': int(request.POST.get('FLAG_PARASITOSIS_INTESTINAL', 0)),
            'FLAG_EXAMEN_PESQUISA_TRASTORNOS_CARDIOVASCULARES': int(request.POST.get('FLAG_EXAMEN_PESQUISA_TRASTORNOS_CARDIOVASCULARES', 0)),
            'FLAG_ADMINISTRACION_DE_FACTOR_VIII_ENDOVENOSO': int(request.POST.get('FLAG_ADMINISTRACION_DE_FACTOR_VIII_ENDOVENOSO', 0)),
            'FLAG_DEFICIENCIA_HEREDITARIA_DEL_FACTOR_VIII': int(request.POST.get('FLAG_DEFICIENCIA_HEREDITARIA_DEL_FACTOR_VIII', 0)),
            'FLAG_NEUMONIA_NO_ESPECIFICADA': int(request.POST.get('FLAG_NEUMONIA_NO_ESPECIFICADA', 0))
        }

        # Convertir el diccionario de entrada en una lista de listas
        datos_de_entrada_lista = [[valor for valor in datos_de_entrada.values()]]

        # Hacer predicciones de probabilidad en lugar de predicciones de clase
        probabilidades_prediccion = modelo.predict_proba(datos_de_entrada_lista)

        # Obtener la probabilidad de la clase positiva (1)
        probabilidad_clase_positiva = probabilidades_prediccion[0][1]

        # Convertir la probabilidad a porcentaje
        porcentaje_prediccion = probabilidad_clase_positiva * 100

        return render(request, 'resultado_prediccion.html', {'porcentaje_prediccion': porcentaje_prediccion})
    #else:
        # Manejar el caso donde no se enviaron datos
        return HttpResponse("Error: Método no permitido")

def evaluacion(request):

    return render(request, "evaluacion.html")



"""
def pruebahola(request):
    return HttpResponse("Hola ")

def evaluacion(request):

    return render(request, "evaluacion.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Mostrar un mensaje de error
            pass
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
"""