import imp
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import carousel, flashNews, GoiInitiative, Studentworks, Faculty, Noticeboard, Tender, Downloads


# Create your views here.

facultyDetails = Faculty.objects.all()
carouselImages = carousel.objects.all()
flashnewss = flashNews.objects.all()
goiInitative = GoiInitiative.objects.all()
studentsWork = Studentworks.objects.all()
tenderData = Tender.objects.all()
noticeData = Noticeboard.objects.all()
downloadsData = Downloads.objects.all()
current_datetime = datetime.now()

context = {
    'siteTitle': 'योजना तथा वास्तुकला विद्यालय विजयवाड़ा | School of Planning And Architecture Vijayawada',
    'carouselImages': carouselImages,
    'flashnewss': flashnewss,
    'goiInitative': goiInitative,
    'studentsWork': studentsWork,
    'current_datetime': current_datetime,
    'facultyDetails': facultyDetails,
    'noticeData': noticeData,
    'tenderData': tenderData,
    'downloadsData': downloadsData,
}


def home(request):
    return render(request, 'home.html', context)


def faculty(request):
    return render(request, 'faculty.html', context)


def noticeboard(request):
    return render(request, 'noticeboard.html', context)


def about(request):
    return render(request, 'about.html', context)


def academics(request):
    return render(request, 'academics.html', context)


def downloads(request):
    return render(request, 'downloads.html', context)


def recruitment(request):
    return render(request, 'recruitment.html', context)


#==========search functionality==========#
def search(request):
    return HttpResponse('Your Search Result')
#==========search functionality==========#
