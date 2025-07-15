from django.db import models

# Create your models here.
class Employee(models.Model):
    """Registro de empleados"""
    
    Nombre_completo=models.CharField(verbose_name='Nombre',max_length=90)
    Email_corporativo=models.EmailField(max_length=254)
    Teléfono=models.CharField(verbose_name='Telefono',max_length=50)
    Cargo=models.CharField(verbose_name='Cargo',max_length=50)
    Departamento=models.CharField(verbose_name='Departamento',max_length=50) 
    Fecha_de_contratación=models.DateTimeField(auto_now_add=True)
    Salario=models.DecimalField(max_digits=10, decimal_places=2)
    Estado=models.BooleanField(default=False)
    
    def __str__(self):
        return f'Empleado: {self.Nombre_completo} - Cargo: {self.Cargo} - Fecha {self.Fecha_de_contratación}'
    
    
    class Meta:
        verbose_name = 'Empleados'
        verbose_name_plural = 'Empleados'
        
        
        
        