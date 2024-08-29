from django.shortcuts import render,redirect

from .models import Teacher

from .forms import TeacherForm





# Create your views here.

def index(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher/index.html",{'teachers':teachers})

def edit(request, pk):
    teacher = Teacher.objects.get(id=pk)
    if request.method == "POST":
        teacher = Teacher.objects.get(id=pk)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher:index')
    else:
        
        teachers = TeacherForm(instance=teacher)
        
        
        context = {'teachers':teachers}
        return render(request, "teacher/edit.html",context)

def add(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher:index')  # Redirect to users list after successful form submission.
        else:
            forms = TeacherForm()
            context= {'form':forms}
            context= {'error': "Invalid field submitted",'form':forms}
            return render(request, "teacher/add.html",context)
    else:
        forms = TeacherForm()
        context= {'form':forms}
        return render(request, "teacher/add.html",context)
    
def delete(request, pk):
    teacher = Teacher.objects.get(id=pk)
    teacher.delete()
    
    return redirect('teacher:index')
    

