from django.conf.urls import url
from . import views
from .views import StudentCreateView, StudentUpdateView, CallofrollCreateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
    # /lycee/student/73
    
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    
    url(r'^student/updatestudent/(?P<pk>\d+)$', StudentUpdateView.as_view(), name='update_student'),
    
    url(r'^callofroll/(?P<cursus_id>[0-9]+)$', views.detail_callofroll, name='detail_callofroll'), 
    
    url(r'^callofroll/create/$', CallofrollCreateView.as_view(), name='callofroll_create'),
    
    url(r'^absence/(?P<cursus_id>[0-9]+)$', views.detail_absence, name='detail_absence'),

    url(r'^absence/student/(?P<student_id>[0-9]+)$', views.detail_student_absence, name='detail_student_absence'),  
]
