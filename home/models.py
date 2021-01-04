from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField(max_length=254)
    picture = models.ImageField(upload_to='profilePicture')
    bio = models.CharField(max_length=2048, null=True, blank=True)
    phone = models.IntegerField()
    github_handle = models.CharField(max_length=256)
    user_type = models.CharField(max_length=11, choices=(('admin', 'admin'), ('contributor', 'contributor')))

    def __str__(self):
        return self.name


class Visitor(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField(max_length=254)
    subscribe = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactIcon(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='icons') # ToDo : Change to Font Awesome Icon Drop Down
    url = models.URLField(max_length=2048, null=True, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=512)
    message = models.CharField(max_length=1024)
    datetime = models.DateTimeField(auto_now_add=True)
    readstatus = models.BooleanField(default=False)

    def __str__(self):
        return self.name+' '+self.email


class Technology(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='badges')

    def __str__(self):
        return self.name


class Project(models.Model):
    Deployed = [('yes', 'yes'), ('no', 'no')]
    Source = [('open', 'open'), ('close', 'close')]
    name = models.CharField(max_length=255, null=False, blank=False)
    sourcecode = models.URLField(null=True, blank=True, default=None)
    deployment_url = models.URLField(null=True, blank=True, default=None)
    icon = models.ImageField(upload_to='icons',null=True, blank=True, default='/static/icons/project.png')
    deployed = models.CharField(max_length=8, choices=Deployed, default='no')
    source = models.CharField(max_length=8, choices=Source, default='close')
    project_type = models.CharField(max_length=10, choices=(('solo', 'solo'), ('group', 'group')))
    developers = models.ManyToManyField(Profile)
    tech_stack = models.ManyToManyField(Technology)
    status = models.CharField(max_length=15, choices=(('Completed', 'completed'), ('In Progress', 'in progress')))
    allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CollaboratorVacancy(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reqirement = models.CharField(max_length=10000)

    def __str__(self):
        return self.project.name


class CollaboratorApplication(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=160)
    email = models.EmailField(max_length=254)
    position = models.CharField(max_length=512)
    phone = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)


class Certification(models.Model):
    name = models.CharField(max_length=120)
    c_link = models.CharField(max_length=255, null=True, blank=True)
    issuedby = models.CharField(max_length=130, null=False, blank=False)
    issue_date = models.DateField(null=True, blank=True, default=None)
    expiry_date=models.DateField(null=True,blank=True,default=None)
    text = models.CharField(max_length=200, null=True,blank=True)
    allowed = models.BooleanField(default=False)


class Logger(models.Model):
    ip = models.CharField(max_length=160)
    refer = models.CharField(max_length=120)
    datetime = models.DateTimeField(auto_now_add=True)


class Badge(models.Model):
    name = models.CharField(max_length=120)
    text = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='badges')
    allowed = models.BooleanField(default=False)
    type = models.CharField(max_length=120, choices=(('tech-stack', 'tech-stack'), ('achievement', 'achievement')))

    def __str__(self):
        return self.name