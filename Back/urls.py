from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'comunas', views.ComunaViewSet)
router.register(r'nacionalidades', views.NacionalidadViewSet)
router.register(r'direcciones', views.DireccionViewSet)
router.register(r'autores', views.AutorViewSet)
router.register(r'bibliotecas', views.BibliotecaViewSet)
router.register(r'libros', views.LibroViewSet)
router.register(r'lectores', views.LectorViewSet)
router.register(r'prestamos', views.PrestamoViewSet)

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),

    # CRUD Libros
    path('libros/lista/', views.LibroList.as_view(), name='libro_list'),
    path('libros/nuevo/', views.LibroCreate.as_view(), name='libro_create'),
    path('libros/editar/<int:pk>/', views.LibroUpdate.as_view(), name='libro_update'),
    path('libros/eliminar/<int:pk>/', views.LibroDelete.as_view(), name='libro_delete'),

    # CRUD Autores
    path('autores/lista/', views.AutorList.as_view(), name='autor_list'),
    path('autores/nuevo/', views.AutorCreate.as_view(), name='autor_create'),
    path('autores/editar/<int:pk>/', views.AutorUpdate.as_view(), name='autor_update'),
    path('autores/eliminar/<int:pk>/', views.AutorDelete.as_view(), name='autor_delete'),

    # CRUD Lectores
    path('lectores/lista/', views.LectorList.as_view(), name='lector_list'),
    path('lectores/nuevo/', views.LectorCreate.as_view(), name='lector_create'),
    path('lectores/editar/<int:pk>/', views.LectorUpdate.as_view(), name='lector_update'),
    path('lectores/eliminar/<int:pk>/', views.LectorDelete.as_view(), name='lector_delete'),

    # CRUD Préstamos
    path('prestamos/lista/', views.PrestamoList.as_view(), name='prestamo_list'),
    path('prestamos/nuevo/', views.PrestamoCreate.as_view(), name='prestamo_create'),
    path('prestamos/editar/<int:pk>/', views.PrestamoUpdate.as_view(), name='prestamo_update'),
    path('prestamos/eliminar/<int:pk>/', views.PrestamoDelete.as_view(), name='prestamo_delete'),

    # API REST
    path('api/', include(router.urls)),
]
