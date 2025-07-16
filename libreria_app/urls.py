from django.urls import path
from . import views
urlpatterns = [
    path('',views.login_admin,name='login_admin'),
    path('registro/',views.registro,name='registro'),
    path('empleados/',views.ver_empleado,name='empleados'),
    path('dasboard/',views.dasboard,name='dasboard'),
    path('eliminar/<int:id>/' ,views.eliminar,name='eliminar'),
    path('editar/<int:id>/',views.editar,name='editar'),
    path('editar_admin/<int:id>/',views.editar_empleados_dasboard,name='editar_admin'),
    path('eliminar_admin/<int:id>/',views.eliminar_empleados_dasboard,name='eliminar_admin'),
    path('detail_employee/<int:id>/',views.ver_empleado_detail,name='detail_emp'),
]