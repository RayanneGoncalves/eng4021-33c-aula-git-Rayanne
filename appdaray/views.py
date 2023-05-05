from django.shortcuts import render, redirect 
from .models import Dance
from .models import Passos

def home(request):
  dance = Dance.objects.all()
  passos = Passos.objects.all()
  context = { "dance": dance,"passos": passos }
  return render(request,"home.html",context=context)

def create_dance(request):
  if request.method == "POST":
    if "done" not in request.POST:
      done = False
    else:
      done = True
    Dance.objects.create(
      title=request.POST["title"],
      description=request.POST["description"],
      nome=request.POST["nome"],
      done=done
    )
    return redirect("home")
  return render(request, "dance_form.html")

def create_passos(request):
  if request.method == "POST":
    Passos.objects.create(
      title=request.POST["title"],
      nome=request.POST["nome"],
      sobrenome=request.POST["sobrenome"],
      data=request.POST["data"],
      done=False
    )
    return redirect("home")
  return render(request, "passos_form.html")


def update_dance(request, dance_id):
  dance = Dance.objects.get(id=dance_id)
  if request.method == "POST":
    dance.title = request.POST["title"]
    dance.description = request.POST["description"]
    dance.nome = request.POST["nome"]
    if "done" not in request.POST:
      dance.done = False
    else:
      dance.done = True
    dance.save()
    return redirect ("home")
  context={"dance":dance}
  return render(request,"dance_form.html",context=context)

def delete_dance(request, dance_id):
  dance = Dance.objects.get(id=dance_id)
  if request.method == "POST":
      if "confirm" in request.POST:
        dance.delete()
      return redirect("home")
  return render(request, "delete_form.html", context={"dance": dance})


def update_passos(request, passos_id):
  passos = Passos.objects.get(id=passos_id)
  passos.data = passos.data.strftime('%Y-%m-%d')
  if request.method == "POST":
    passos.title = request.POST["title"]
    passos.nome = request.POST["nome"]
    passos.sobrenome = request.POST["sobrenome"]
    if "done" not in request.POST:
      passos.done = False
    else:
      passos.done = True
    passos.save()
    return redirect ("home")
  context={"passos":passos}
  return render(request,"passos_form.html",context=context)

def delete_passos(request, passos_id):
  passos = Passos.objects.get(id=passos_id)
  if request.method == "POST":
      if "confirm" in request.POST:
        passos.delete()
      return redirect("home")
  return render(request, "delete_passos_form.html", context={"passos": passos})