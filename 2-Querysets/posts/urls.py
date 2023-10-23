from django.urls import path, re_path
from .views import dummy_view, status_code_view, entry_list,redirect_back_home

app_name = "posts"

urlpatterns = [
    path('', redirect_back_home, name='entry-list'),
    path('<id>/', dummy_view, name='entry-detail'),
    re_path('(?P<id>[0-9]{4})/(?P<slug>[\w-]+)/$', dummy_view, name='entry-detail-2'),
    path('<id>/delete/', dummy_view, name='entry-delete'),
    path('<id>/update/', dummy_view, name='entry-update')
]



            # EJEMPLO DE SLUG
#   poost - title: "Nuevo Titulo para el articulo"
#         - slug: "https://datadosis.com/entries/nuevo-titulo-para-el-articulo"

            #   EJEMPLO DE URLS CON EXPRESIONES REGULARES