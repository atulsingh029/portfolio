from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField(max_length=254)
    picture = models.ImageField(upload_to='profilePicture')
    bio = models.CharField(max_length=2048, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    github_handle = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class ContactIcon(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    icon = models.CharField(max_length=50,help_text="enter font awesome icon name")
    url = models.URLField(max_length=2048, null=True, blank=True)

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


class TechStack(models.Model):
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
    icon = models.ImageField(upload_to='icons',null=True, blank=True, default='icons/project.png')
    deployed = models.CharField(max_length=8, choices=Deployed, default='no')
    source = models.CharField(max_length=8, choices=Source, default='close')
    project_type = models.CharField(max_length=10, choices=(('solo', 'solo'), ('group', 'group')))
    project_domain = models.CharField(max_length=50)
    developers = models.ManyToManyField(Profile)
    tech_stack = models.ManyToManyField(TechStack)
    status = models.CharField(max_length=15, choices=(('Completed', 'completed'), ('In Progress', 'in progress')))
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    allowed = models.BooleanField(default=False)
    description = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.name


class ProjectScreenshot(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/screenshots', null=True, blank=True)
    first = models.BooleanField(default=False)

    def __str__(self):
        return self.project.name


class ProjectRelatedDoc(models.Model):
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=50, default='file', null=True, blank=True)
    document = models.FileField(upload_to='doc/')
    type = models.CharField(max_length=100, choices=(('public', 'public'), ('private', 'private')))

    def __str__(self):
        return self.project.name + " Document : " +str(self.name)


class Certification(models.Model):
    name = models.CharField(max_length=120)
    c_link = models.CharField(max_length=255, null=True, blank=True)
    issuedby = models.CharField(max_length=130, null=False, blank=False)
    issue_date = models.DateField(null=True, blank=True, default=None)
    expiry_date=models.DateField(null=True,blank=True,default=None)
    text = models.CharField(max_length=200, null=True,blank=True)
    allowed = models.BooleanField(default=False)


class Experience(models.Model):
    company_name = models.CharField(max_length=120)
    experience_type = models.CharField(max_length=50, choices=[('internship','Internship'),('fullTimeJob', 'Full-Time Job'),('freelance', 'Freelance')])
    role = models.CharField(max_length=255, null=True, blank=True)
    project = models.CharField(max_length=130, null=True, blank=True)
    project_url = models.URLField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True, default=None)
    to_date=models.DateField(null=True,blank=True,default=None)
    text = models.CharField(max_length=200, null=True,blank=True)
    allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


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