from django.shortcuts import render
from django.http import HttpResponse

def CCMS_Mission(request):
    title = "Mission"
    content = "The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence."
    return render(request, "Ccms.html", {'title':title ,'content':content})

def CCMS_Vision(request):
    content = "The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education."
    return render(request, "Ccms.html", {'content':content})

def CCMS_Objectives(request):
    content = """ Be employes and demonstrate professionalism, competence and passion in solving contemporary comuting problems by developing or utilizing innovative IT solutions. 
    Embark in lifelong learning or research to attune to the continuous innovation in the IT industry in order to adapt to the changing demands of the global market.
    Exhibit leadership and teamwork, and commitment to their respective local or global organizations. """
    return render(request, "Ccms.html", {'content':content})

