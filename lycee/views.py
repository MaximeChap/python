from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cursus,Student,Presence
from .form import StudentForm,CallOfRollForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404


#def index(request):
#  return HttpResponse("Racine de lycee")

# index : utilisation de HttpResponse
#def index(request):
#  result_list = Cursus.objects.order_by('name')
#  # chargement du template
#  template = loader.get_template('lycee/index.html')
#  # contexte
#  context = { 'liste' : result_list}
#  return HttpResponse(template.render(context, request))

# index : variante avec template intEgrE
def index (request):
  result_list = Cursus.objects.order_by('name')
  # contexte
  context = { 'liste' : result_list}
  # utilisation du template intEgrE
  return render (request, 'lycee/index.html', context)

def detail(request,cursus_id):
    result_list = Student.objects.all().filter(cursus = cursus_id)
    # context
    result_cursus_list = get_object_or_404(Cursus, pk=cursus_id)
    context = {'liste': result_list, 'liste_cursus' : result_cursus_list}
    return render (request, 'lycee/detail_cursus.html' , context)

def detail_student(request,student_id):
    #result_list = Student.objects.get(pk=student_id)
    result_list = get_object_or_404(Student, pk=student_id)
    # context
    context = {'liste': result_list,}
    return render (request, 'lycee/student/detail_student.html' , context)

def detail_callofroll(request,cursus_id):
    result_list = Student.objects.all().filter(cursus = cursus_id)
    # context
    result_cursus_list = get_object_or_404(Cursus, pk=cursus_id)
    context = {'liste': result_list, 'liste_cursus' : result_cursus_list}
    return render (request, 'lycee/detail_callofroll.html' , context)

class StudentCreateView(CreateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/create.html"

  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

class StudentUpdateView(UpdateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/updatestudent.html"
  
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))


class CallofrollCreateView(CreateView):
  # ref au modEle
  model = Presence
  # ref au formulaire
  form_class = CallOfRollForm
  # le nom du render
  template_name = "lycee/create_callofroll.html"

  # page si creation ok
  def get_success_url(self):
    return reverse ("index", args=(self.object.pk,))





  
    
