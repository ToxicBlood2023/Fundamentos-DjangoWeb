

from django.urls import path, re_path
from .views import (
                    entry_list_view,
                    EntryClassView,
                    post_create
)

app_name = "posts"

urlpatterns = [
    path('', entry_list_view, name='entry-list'),
    path('create/', post_create, name='entry-create'),
    path('class-view/', EntryClassView.as_view(), name='entry-class-list'),
]













            # EJEMPLO DE SLUG
#   poost - title: "Nuevo Titulo para el articulo"
#         - slug: "https://datadosis.com/entries/nuevo-titulo-para-el-articulo"

            #   EJEMPLO DE URLS CON EXPRESIONES REGULARES