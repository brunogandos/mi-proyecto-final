from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html",{"nombre":"Bruno"})

def index_2(request,nombre,apellido):
    return render(request, "ejemplo/saludar.html",
        {
            "nombre":nombre,
            "apellido": apellido   
        })

def index_3(request):
    return render(request, "ejemplo/saludar.html",
    {
        "notas": [1,2,3,4,5,6,7,8]
    })

def imc(request,peso,altura):
    imc = 1
    return render(request,"ejemplo/imc.html",{"imc": imc})

