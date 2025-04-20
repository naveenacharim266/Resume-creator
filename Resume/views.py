from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from .models import BasicDetails, Experince, Education, Project, Skills, Certifications
import pdb
# Create your views here.
@csrf_exempt
def AddBasicDetails(request):
    if request.method =="POST":
        data = json.loads(request.body)
        
        try:
            basicdetails=BasicDetails.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                phone=data.get('phone'),
                summary=data.get('summary'),
                linkedin=data.get('linkedin'),
                github=data.get('github'),
                website=data.get('website')
            )
            return HttpResponse({"status":"success", "id":basicdetails.id})
        except Exception as e:
            return HttpResponse({"status":"error", "message":str(e)}, status=400)    
    else:
        return HttpResponse({"message":"only post is allowed"}, status=405)
    
@csrf_exempt
def AddExperince(request):
    
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            Experince.objects.create(
                title = data.get('title'),
                employment_type = data.get('employment_type'),
                organization = data.get('organization'),
                startdate = data.get('startdate'),
                enddate = data.get('enddate'),
                location = data.get('location'),
                location_type = data.get('location_type'),
                description = data.get('description'),
                skills_used = data.get('skills_used')
            )
            return HttpResponse({'status':'success','message':"Saved Successfully"})
        except Exception as e:
            return HttpResponse({'status':'error','message':str(e)},status=400)
    else:
        return HttpResponse({"status":"error", "message":"only post is allowed"},status=405)

@csrf_exempt
def AddProject(request):
    
    if request.method=='POST':
        data = json.loads(request.body)
        try:
            Project.objects.create(
                project_title=data.get('project_title'),
                role = data.get('role'),
                client = data.get('client'),
                startdate = data.get('startdate'),
                enddate = data.get('enddate'),
                project_details = data.get('project_details')
                
            )
            return HttpResponse({'status':'success', 'message':'Project saved successfully!'})
        except Exception as e:
            return HttpResponse({'status':'error', 'message':str(e)}, status=400)
    else:
        return HttpResponse({'status':'error', 'message':'only post is allowed'}, status=405)       

@csrf_exempt
def AddSkills(request):
    if request.method =='POST':
        data = loads.json(request.body)
        try:
            Skills.objects.create(
                name = data.get('name')
            )
            return HttpResponse({'status':'success', 'message':'Skills saved successfully'})
        except Exception as e:
            return HttpResponse({'status':'error', 'message':str(e)})
            
@csrf_exempt 
def AddEducation(request):   
    if request.method =="POST":
        data = loads.json(request.body)
        try:
            Education.objets.create(
                degree = data.get('degree'),
                university = data.get('university'),
                course = data.get('course'),
                specialization = data.get('specialization'),
                course_type = data.get('course_type'),
                course_duration = data.get('course_duration'),
                grading_system = data.get('grading_system'),
                marks = data.get('marks'),
                
            )
            return HttpResponse({'satus':'success', 'message':'Education saved successfuly'})
        except Exception as e:
            return HttpResponse({'status':'error','message':'Education not saved'})
    else:
        return HttpResponse({'status':'error','message':'Only post method is allowed'},status=405)        
                