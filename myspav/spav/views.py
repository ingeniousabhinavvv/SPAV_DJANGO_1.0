import imp
from multiprocessing import context
from django.shortcuts import render
from datetime import datetime
from .models import carousel, flashNews, GoiInitiative, Studentworks, Faculty, Noticeboard


# Create your views here.

facultyDetails = Faculty.objects.all()
carouselImages = carousel.objects.all()
flashnewss = flashNews.objects.all()
goiInitative = GoiInitiative.objects.all()
studentsWork = Studentworks.objects.all()
noticeData = Noticeboard.objects.all()
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
}


def home(request):
    return render(request, 'home.html', context)


def faculty(request):
    return render(request, 'faculty.html', context)


def noticeboard(request):
    return render(request, 'noticeboard.html', context)
