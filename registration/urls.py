from django.conf.urls import url, patterns
from registration import views

urlpatterns = patterns('',
	url(r'^save_student_details/',views.save_student_details,name='save_student_details'),
	url(r'^std_list/', views.std_list,name="std_list"),
    url(r'^index/', views.index,name='index'),
    url(r'^delete_student_details/',views.delete_student_details,name='delete_student_details'),
    # url(r'^edit/',views.edit,name='edit')
)
