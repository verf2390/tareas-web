from django.urls import path
from .views import lista_pendientes
from .views import detalle_tarea
from .views import crear_tarea
from .views import editar_tarea
from .views import eliminar_tarea
from .views import logueo, pagina_registro
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [path('', lista_pendientes.as_view(), name ='tareas'),
               path('login/', logueo.as_view(), name ='login'),
               path('registro/', pagina_registro.as_view(), name ='registro'),
               path('logout/', LogoutView.as_view(next_page='login'), name ='logout'),
               path('tarea/<int:pk>', detalle_tarea.as_view(), name ='tarea'),
               path('crear_tarea/', crear_tarea.as_view(), name ='crear_tarea'),
               path('editar_tarea/<int:pk>', editar_tarea.as_view(), name ='editar_tarea'),
               path('eliminar_tarea/<int:pk>', eliminar_tarea.as_view(), name ='eliminar_tarea'),
               path('toggle-completo/<int:pk>/', views.toggle_completo, name='toggle_completo'),
               ]
]
