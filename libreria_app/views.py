from django.shortcuts import render,redirect,get_object_or_404
from . models import Employee
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

# Create your views here.
def registro(request):
    if request.method == 'POST':
        Nombre_completo = request.POST['Nombre_completo']
        
        Email_corporativo = request.POST['Email_corporativo']
        
        Teléfono = request.POST['Teléfono']
        
        Cargo = request.POST['Cargo']
        Departamento = request.POST['Departamento']
        Fecha_de_contratación = request.POST['Fecha_de_contratación']
        Salario = request.POST['Salario']
        Estado = request.POST['Estado']
        
        Employee.objects.create(Nombre_completo= Nombre_completo,Email_corporativo=Email_corporativo,Teléfono=Teléfono,Cargo=Cargo,Departamento=Departamento,Fecha_de_contratación=Fecha_de_contratación,Salario=Salario,Estado=Estado)
        return render(request,'registro.html')
        
    return render(request,'registro.html')


def ver_empleado(request):
        
    emp =  Employee.objects.all()
    return render(request,'list_emp.html',{
        'emp':emp
    })

def ver_empleado_detail(request, id):
    emp = Employee.objects.filter(id=id)
    return render(request,'list_emp.html',{
        'emp':emp
    })        
        
    
def eliminar(request,id):
    usuario = get_object_or_404(Employee,id=id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente')
        return render (request,'dasboard.html')
    return render(request,'list_emp.html',{
        'usuario':usuario
        
    })

def editar(request, id):
    empleado = get_object_or_404(Employee, id=id)
    
    if request.method == 'POST':
        empleado.Nombre_completo = request.POST['Nombre_completo']
        empleado.Email_corporativo = request.POST['Email_corporativo']
        empleado.Teléfono = request.POST['Teléfono']
        empleado.Cargo = request.POST['Cargo']
        empleado.Departamento = request.POST['Departamento']
        empleado.Fecha_de_contratación = request.POST['Fecha_de_contratación']
        empleado.Salario = request.POST['Salario']
        
        #  convertir string a boolean
        estado_str = request.POST['Estado']
        empleado.Estado = True if estado_str == 'Activo' else False
        
        empleado.save()
        
        messages.success(request, 'Empleado actualizado exitosamente')
        return redirect('empleados')
    
    return render(request, 'editar_empleado.html', {'empleado': empleado})

def eliminar_empleados_dasboard(request, id):
    emp = Employee.objects.all()
    empleado = get_object_or_404(Employee,id=id)
    if request.method == 'POST':
        empleado.delete()
        messages.success(request, 'Usuario eliminado exitosamente')
        return render (request,'dasboard.html')
    return render(request,'list_emp.html',{
        'emp':emp,
        'empleado':empleado,
    }
        
    )
        
def editar_empleados_dasboard(request, id):
      empleado = get_object_or_404(Employee, id=id)
      
      if request.method == 'POST':
                empleado.Nombre_completo = request.POST['Nombre_completo']
                empleado.Email_corporativo = request.POST['Email_corporativo']
                empleado.Teléfono = request.POST['Teléfono']
                empleado.Cargo = request.POST['Cargo']
                empleado.Departamento = request.POST['Departamento']
                empleado.Fecha_de_contratación = request.POST['Fecha_de_contratación']
                empleado.Salario = request.POST['Salario']
                
                #convertir string a boolean
                estado_str = request.POST['Estado']
                empleado.Estado = True if estado_str == 'Activo' else False
                
                empleado.save()
                
                messages.success(request, 'Empleado actualizado exitosamente')
                return redirect('empleados')
            
        
      return render(request, 'editar_empleado.html', {'emp': empleado})

    
        

    
def dasboard(request):
    emp = Employee.objects.all()
    return render(request,'dasboard.html',{
        'emp':emp
    })

