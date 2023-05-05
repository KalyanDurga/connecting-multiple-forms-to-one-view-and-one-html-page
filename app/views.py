from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse


def insert_data(request):
    TFO=TopicForm()
    WFO=WebpageForm()
    ARO=AccessrecordForm()
    d={'TFO':TFO,'WFO':WFO,'ARO':ARO}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        WFD=WebpageForm(request.POST)
        ARD=AccessrecordForm(request.POST)
        if TFD.is_valid() and WFD.is_valid() and ARD.is_valid():
            NSTO=TFD.save(commit=False)
            NSTO.save()

            NSWO=WFD.save(commit=False)
            NSWO.topic_name=NSTO
            NSWO.save()

            NSAO=ARD.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()
            
            return HttpResponse('Data inserted successfully')
        else:
            return HttpResponse('Not a valid data')


    return render(request,'insert_data.html',d)