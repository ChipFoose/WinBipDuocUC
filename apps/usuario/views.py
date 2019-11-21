from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyDmzZsjKBCzqAHYGPQesENd2GPkgM436p0",
    'authDomain': "winbipduocuc.firebaseapp.com",
    'databaseURL': "https://winbipduocuc.firebaseio.com",
    'projectId': "winbipduocuc",
    'storageBucket': "winbipduocuc.appspot.com",
    'messagingSenderId': "590854125477",
    'appId': "1:590854125477:web:a74ceb8b0f2eae490a9a4c",
    'measurementId': "G-FMV0HQHKTK"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
database = firebase.database()


def PaginaInicio(request):
    return render(request, 'usuario/index.html')


def Premios(request):
    return render(request, 'usuario/premios.html')


def Registro(request):
    return render(request, 'usuario/registro.html')


def IniciarSesion(request):
    return render(request, 'usuario/iniciarsesion.html')


def postsignup(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    user = auth.sign_in_with_email_and_password(email, passw)

    return render(request, 'usuario/welcome.html')


def signup(request):
    nombre = request.POST.get('nombre')
    apaterno = request.POST.get('apaterno')
    amaterno = request.POST.get('amaterno')
    rut = request.POST.get('rut')
    nbip = request.POST.get('nbip')
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    user = auth.create_user_with_email_and_password(email, passw)

    uid = user['localId']

    data = {"Nombre": nombre, "Apellido paterno": apaterno, "Apellido materno": amaterno,
            "Rut": rut, "Número de bip": nbip, "Correo electrónico": email, "Contraseña": passw}

    database.child("Usuarios").child(uid).child(
        "Detalles de los usuarios").set(data)
    return render(request, 'usuario/welcome.html')
