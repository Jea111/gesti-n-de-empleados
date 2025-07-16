from django.contrib import admin
from .models import Employee,LoginAmin

class EmployeeAdmin(admin.ModelAdmin):
    # Controla qué campos se muestran en el FORMULARIO de edición/creación
    fields = ['Nombre_completo', 'Email_corporativo', 'Cargo', 'Departamento', 'Teléfono', 'Salario', 'Estado']
    
    #   Controla qué columnas se muestran en la LISTA de registros
    list_display = ['Nombre_completo', 'Cargo', 'Departamento', 'Estado', 'Fecha_de_contratación']
    
    #   Agrega FILTROS en la barra lateral derecha
    list_filter = ['Cargo', 'Departamento', 'Estado', 'Fecha_de_contratación']
    
    #   Agrega una CAJA DE BÚSQUEDA en la parte superior
    search_fields = ['Nombre_completo', 'Email_corporativo', 'Cargo']

admin.site.register(Employee, EmployeeAdmin)



    
    
class LoginAdmin(admin.ModelAdmin):
    """Login de administradores para la dashboard"""
    fields = ['username','password']
    list_display = ['username','password']
    list_filter = ['username','password']
    search_fields = ['username']
admin.site.register(LoginAmin,LoginAdmin)
