from django.db import models


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)

    location = models.TextField(null=True)

    title = models.CharField(max_length=100, null=True)
    summary = models.TextField(null=True)

    photo = models.ImageField(upload_to='profile_pics', null=True)

    major = models.CharField(max_length=100, null=True)

    birthday = models.DateField(null=True)
    website_url = models.URLField(null=True)
    # degree = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)

    github_url = models.URLField(max_length=100, null=True)
    linkedin_url = models.URLField(max_length=100, null=True)

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='skill', null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100, null=True)
    university = models.CharField(max_length=100)
    entered_date = models.DateField()
    graduation_date = models.DateField()

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='education', null=True)

    def __str__(self):
        return '{} of {}'.format(self.degree, self.university)


class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    entered_date = models.DateField()
    finished_date = models.DateField()
    location = models.CharField(max_length=100, null=True, blank=True)

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='experience', null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{} of {}'.format(self.position, self.company)


class ExperienceItem(models.Model):
    description = models.TextField()
    experience = models.ForeignKey('Experience', on_delete=models.CASCADE, related_name='experience_item', null=True)

    def __str__(self):
        return '{}'.format(self.description)


class Project(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='project', null=True)
    type = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    image = models.ImageField(upload_to='profiles/')
    github_url = models.URLField()

    def __str__(self):
        return self.title


class MyMail(models.Model):
    from_name = models.CharField(max_length=100)
    from_email = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return '{} - {}'.format(self.from_name, self.subject)

class AccessLog(models.Model):
    ipaddress = models.CharField(max_length=100)
    count = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return '{} - {}'.format(self.ipaddress, self.count)