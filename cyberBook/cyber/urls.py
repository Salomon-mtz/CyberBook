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

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.custom_logout, name='logout'),
    path('reservas/', views.reservas, name='reservas'),
    path('', include(router.urls)),
    path('espacios/', include('rest_framework.urls', namespace='rest_framework1')),
    path('softwares/', include('rest_framework.urls', namespace='rest_framework2')),
    path('reservaUser/', include('rest_framework.urls', namespace='rest_framework3')),
    path('equipos/', include('rest_framework.urls', namespace='rest_framework4')),
    path('espacios/<int:id>', views.espacios),
    path('softwares/<int:id>', views.software),
    path('equipos/<int:id>', views.equipos),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)