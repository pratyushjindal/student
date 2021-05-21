# from django.shortcuts import re
from django.http import HttpResponseRedirect
import json
from django.shortcuts import render,render_to_response

from registration import models
# Create your views here.

def std_list(request):
    student_list = models.info.objects.all()
    student_dict ={'info':student_list}
    return render(request,'registration/list.html',context=student_dict)

def list(request):
	student_list = models.info.objects.all()
	student_dict={'info':student_list}
	return render(request,'registration/home.html',context=student_dict)
def index(request):
	# if 'id' in request.GET:
	# 	student_id = request.GET['id']
	# 	data = models.info.objects.filter(id=student_id).first()
	# 	return render_to_response('registration/home.html',{'data':data})
	return render_to_response('registration/home.html')

# def edit(request):

	
	
# 	return render(request,'registration/edit.html')
def delete_student_details(request):
    student_id= request.GET['id']
    print "22"
    info_data = models.info.objects.filter(id=int(student_id)).first()
    info_data.delete()
    return HttpResponse(json.dumps("Delete Successfully"))

def save_student_details(request):
    student_name = request.GET['student_name']
    student_admin = request.GET['student_admin']
    student_mob = request.GET['student_mob']
    student_standard = request.GET['student_standard']
    section = request.GET['section']
    # print "arrararra",student_name
    # print student_standard
    # print student_mob
    # print student_mob
    # print section
    if 'id' in request.GET:
        student_id = request.GET['id']
        print "===========================",type(student_id),student_id,request.GET
    	info_data = models.info.objects.filter(id=int(student_id)).first()
    else:
    	info_data = models.info()
    info_data.FullName = student_name
    info_data.PhoneNo = student_mob
    info_data.AdmissionNo = student_admin
    info_data.Standard = student_standard
    info_data.Section = section
    info_data.save()
    

    # info_data = models.info()
    # info_data.FullName = student_name
    # info_data.save()
    # info_obj=models.info.objects.all()
    # print "nasf========",len(info_obj)
    # for i in info_obj:
    # 	print i.id,i.FullName,i.PhoneNo
    student_list = models.info.objects.all()
    student_dict = {'info':student_list}
    return render(request,'registration/home.html',context=student_dict)
    # models
    # return HttpResponse(json.dumps("done"))


