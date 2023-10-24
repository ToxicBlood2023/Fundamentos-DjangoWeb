from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
import datetime
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Entry, Blog
from .forms import BlogModelForm, BlogForm


def dummy_view(request, id):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now} and the id is {id} </body></html>"
    return HttpResponse(html)


def status_code_view(request, exception):
    return HttpResponseNotFound("Pagina Web no Encontrada, error 404")


def entry_list_view(request):
    entries = Entry.objects.all()
    blog_list = Blog.objects.all()
    context={
        'post_list':entries,
        'blog_list':blog_list
    }
    return render(request, "posts/post_list.html",context)

class EntryClassView(ListView):
    model = Entry
    context_object_name = 'post_list'
    template_name = 'post_list.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newVariable'] = 1234
        return context
    
    def get_queryset(self):
        # filtrando
        return Entry.objects.all()[0:1]
    
    
class EntryClassDetailView(DetailView):
    model = Entry
    
    def get_objects(self):
        obj = super().get_object()
        # realizar logica
        return obj


def post_create(request):
    # form = BlogForm(request.POST or None)
    # if form.is_valid():
    #     name=form.cleaned_data.get('name')
    #     tagline= form.cleaned_data.get('tagline')
    #     blog= Blog(name=name,tagline=tagline)
    #     blog.save()
    #     return redirect('entries:entry-list')
    form = BlogModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('entries:entry-list')
    context={
        'form':form
    }
    return render(request, "form.html", context)
    
    
    
    
def redirect_back_home(request):
    return redirect("/entries/1")


class MyClassView(View):
    def get(self, request):
        print("correr codigo")
        return HttpResponse("Response from a CBV")
    
    
class MyListView(ListView):
    model = Entry