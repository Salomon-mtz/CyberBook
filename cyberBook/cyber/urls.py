from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from cyber import views

router = routers.DefaultRouter()
router.register(r'espacios', views.EspaciosViewSet)
router.register(r'softwares', views.SoftwaresViewSet)
router.register(r'reservaUser', views.ReservaViewSet)
router.register(r'equipos', views.EquiposViewSet)
router.register(r'usuarios', views.UsuarioViewSet)

urlpatterns = [
path('LoginApp', views.hacerLoginApp, name='LoginApp'),
    path('getUsuariosApp', views.getUsuariosApp, name='getUsuariosApp'),
    path('registrarUsApp', views.registrarUsuarioApp, name='registrarUsApp'),
    path('enviarMail', views.enviarMail, name='enviarMail'),
    path('logoutApp', views.logoutApp, name='logoutApp'),
    path('resvSp', views.getReserva, name='resvSp'),
    path('getData', views.getData, name='getData'),
    path('getStats', views.getStats, name='getStats'),
    
    
    path('api/', include(router.urls)),
    path('usuarios/', include('rest_framework.urls', namespace='rest_framework5')),
    path('users/', include('rest_framework.urls', namespace='rest_framework6')),


    path('', views.index, name='index'),
    path('login/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.custom_logout, name='logout'),
    path('reservas/', views.reservas, name='reservas'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('verificaEmail/', views.verificaEmail, name='verificaEmail'),
    path('', include(router.urls)),
    path('espacios/', include('rest_framework.urls', namespace='rest_framework1')),
    path('softwares/', include('rest_framework.urls', namespace='rest_framework2')),
    path('reservaUser/', include('rest_framework.urls', namespace='rest_framework3')),
    path('equipos/', include('rest_framework.urls', namespace='rest_framework4')),
    path('espacios/<int:id>', views.espacios),
    path('softwares/<int:id>', views.software),
    path('equipos/<int:id>', views.equipos),
    path('reservaEsp/<int:espacio_id>', views.reservaEsp, name='reservaEsp'),
    path('reservaEq/<int:equipo_id>', views.reservaEq, name='reservaEq'),
    path('reservaSoft/<int:software_id>', views.reservaSoft, name='reservaSoft'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)