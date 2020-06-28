from django.db import models


class Visitor(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField(max_length=254)
    subscribe = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=512)
    message = models.CharField(max_length=1024)
    datetime = models.DateTimeField(auto_now_add=True)
    readstatus = models.BooleanField(default=False)

    def __str__(self):
        return self.name+' '+self.email


class Carousel(models.Model):
    CHOICES = [('active', 'active'),]
    name = models.CharField(max_length=120)
    carouselimg = models.CharField(max_length=255, unique=True, null=False, blank=False)
    carouselappname = models.CharField(max_length=50, null=True, blank=True)
    carouselapplink = models.CharField(max_length=255, null=True, blank=True)
    active = models.CharField(max_length=6,choices=CHOICES, null=True, blank=True, default=None)
    issuedby = models.CharField(max_length=130, null=False, blank=False)
    allowed = models.BooleanField(default=False)
    iscertificate = models.BooleanField(default=False)


    @staticmethod
    def getCarousel():
        craouselsObj = Carousel.objects.all()
        craousels = []
        for i in craouselsObj:
            if i.allowed:
                temp = {'carouselimg': i.carouselimg, 'carouselapplink': i.carouselapplink,
                        'carouselappname': i.carouselappname, 'active': i.active,
                        'issuedby':i.issuedby, 'iscertificate':i.iscertificate,
                        'name':i.name,}
                craousels.append(temp)
        return craousels

    def __str__(self):
        return self.name


class ProjectCards(models.Model):
    CHOICES = [('active', 'active'), ]
    CSS = [('disabled', 'disabled'), ]

    name = models.CharField(max_length=255, null=False, blank=False)
    sourcecode = models.URLField(null=True, blank=True, default=None)
    applink = models.URLField(null=True, blank=True, default=None)
    icon = models.URLField(null=True, blank=True, default='https://atulsingh029.github.io/icons/pcdefault.png')
    description = models.CharField(max_length=160, null=True, blank=True, default='')
    allowed = models.BooleanField(default=False)
    active = models.CharField(max_length=6, choices=CHOICES, null=True, blank=True, default=None)
    appstatus = models.CharField(max_length=8, choices=CSS, null=True, blank=True, default=None)
    sourcestatus = models.CharField(max_length=8, choices=CSS, null=True, blank=True, default=None)


    @staticmethod
    def getProjectCards():
        projectObj = ProjectCards.objects.all()
        projects = []
        for i in projectObj:
                temp = {'name': i.name, 'applink': i.applink,
                        'sourcecode': i.sourcecode, 'active': i.active,
                        'icon': i.icon, 'description': i.description,
                        'appstatus' : i.appstatus, 'sourcestatus': i.sourcestatus,
                        'allowed':i.allowed
                        }
                projects.append(temp)
        return projects


class Tracking_Logger(models.Model):
    ip = models.CharField(max_length=160)
    refer = models.CharField(max_length=120)
    datetime = models.DateTimeField(auto_now_add=True)