from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='sesion.html'), name='login'),
    path('login/', LoginView.as_view(template_name='lr/sesion.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='lr/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('exit/', views.exit, name='exit'),
    path('tienda/<int:idTienda>', views.tienda, name='tienda'),
    path('', views.index, name='index1'),
    path('index/', views.index, name='index'),
    path('proveedores/<int:idTienda>', views.proveedores, name='proveedores'),
    path('descuentos/<int:idTienda>', views.descuentos, name='descuentos'),
    path('eventos/<int:idTienda>', views.eventos, name='eventos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)