from django.db import models

# Create your models here.


class carousel(models.Model):
    carouselImage = models.ImageField(upload_to='carousel', null=True)
    carouseTitle = models.CharField(max_length=250)

    def __str__(self):
        return self.carouseTitle


class flashNews(models.Model):
    flashTitle = models.CharField(max_length=250)
    flashUrl = models.URLField(max_length=250)

    def __str__(self):
        return self.flashTitle


class GoiInitiative(models.Model):
    goiLogoalt = models.CharField(max_length=250)
    goiLogo = models.ImageField(upload_to='goiinit', null=True)
    goiinitUrl = models.URLField(max_length=250)

    def __str__(self):
        return self.goiLogoalt


class Studentworks(models.Model):
    altText = models.CharField(max_length=250)
    studentworksImage = models.ImageField(upload_to='studentworks', null=True)

    def __str__(self):
        return self.altText


class Faculty(models.Model):
    facultyName = models.CharField(max_length=250, blank=True, null=True)
    facultyProfile = models.ImageField(upload_to='facultyprofile')
    facultyPhone = models.IntegerField()
    facultyEmail = models.EmailField(max_length=250)
    facultyQualification = models.CharField(max_length=250)
    facultyDesignation = models.CharField(max_length=250)
    facultyCv = models.FileField(upload_to='facultycv')
    facultyPublication = models.URLField(max_length=250)
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.facultyName


class Noticeboard(models.Model):
    noticeTitle = models.CharField(max_length=250, blank=True, null=True)
    noticeFile = models.FileField(upload_to='noticeboard')
    noticeTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.noticeTitle

#==========for archive system ==========#


class BasePostModel(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(BasePostModel):
    pass


class PostArchive(BasePostModel):
    pass
