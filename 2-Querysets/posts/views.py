from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
import datetime


def dummy_view(request, id):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now} and the id is {id} </body></html>"
    return HttpResponse(html)


def status_code_view(request, exception):
    return HttpResponseNotFound("Pagina Web no Encontrada, error 404")


def entry_list(request):
    return render(request, "posts/post_list.html",{})

def redirect_back_home(request):
    return redirect("/entries/1")