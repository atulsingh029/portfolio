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
    allowed = models.BooleanField(default=False)

    @staticmethod
    def getCarousel():
        craouselsObj = Carousel.objects.all()
        craousels = []
        for i in craouselsObj:
            if i.allowed:
                temp = {'carouselimg': i.carouselimg, 'carouselapplink': i.carouselapplink,
                        'carouselappname': i.carouselappname, 'active': i.active}
                craousels.append(temp)
        return craousels

    def __str__(self):
        return self.name