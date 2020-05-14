import datetime

from django.db import models
from django.contrib.auth.models import User, Group, UserManager
# from django.utils import timezone

# Create your models here.


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#     def __str__(self):
#         return self.question_text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text


class GSCapabilitySet(models.Model):
    name = models.CharField(max_length=100, default= 'View Only', unique=True)
    load_profile = models.BooleanField(default=False)
    outage_mgmt = models.BooleanField(default=False)
    editing = models.BooleanField(default=False)
    power_flow = models.BooleanField(default=False)
    model_editing = models.BooleanField(default=False)
    batch_delete_selection = models.BooleanField(default = False)

    # the model/class name is used in the admin page to name
    # these modles.  Use Meta class to override
    class Meta:
        verbose_name = 'Map Capability'
        verbose_name_plural = 'Map Capabilities'

    def getList(self):
        return ",".join(["%s:%s"%(a, v) for a, v in self.__dict__.items() if a[0] != '_' and a not in ['id', 'name']])


    def __str__(self):
        return self.name


class GSInstance(models.Model):
    name = models.CharField(max_length=100, default= 'EPE', unique=True)
    gis_server = models.CharField(max_length=100, default= '')
    db_server = models.CharField(max_length=100, default= '')
    db_instance = models.CharField(max_length=100, default= '')
    map_instance = models.CharField(max_length=100, default= '')
    sde_instance = models.CharField(max_length=100, default= '')
    sde_pfx = models.CharField(max_length=100, default= '')
    grid_instance = models.CharField(max_length=100, default= '')
    #capabilities = models.ForeignKey(GSCapabilitySet, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Map Instance'
        verbose_name_plural = 'Map Instances'

    def __str__(self):
        return self.name


# extends Django group
class GSGroup(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    #org = models.ForeignKey(GSOrg, on_delete=models.CASCADE)
    capabilities = models.ForeignKey(GSCapabilitySet, on_delete=models.CASCADE)
    default_instance = models.ForeignKey(GSInstance, on_delete=models.CASCADE, related_name = 'default_instance', null = True)
    instances = models.ManyToManyField(GSInstance, related_name = 'instances')

    class Meta:
        verbose_name = 'ENER-i Group'
        verbose_name_plural = 'ENER-i Groups'

    def __str__(self):
        return self.group.name


# extends Django user
class GSUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #default_instance = models.ForeignKey(GSInstance, on_delete=models.CASCADE)
    #instances = models.ManyToManyField(GSInstance)
    #org = models.ForeignKey(GSOrg, on_delete=models.CASCADE)
    group = models.ForeignKey(GSGroup, on_delete=models.CASCADE)
    # email_confirmed = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        verbose_name = 'ENER-i User'
        verbose_name_plural = 'ENER-i Users'

    def __str__(self):
        return 'select me %s' % self.user.username

    # this is a static class method.
    # I think it overrides the create of GSUser
    @classmethod
    def create(cls, user):
        gsuser = cls(user = user, group = GSGroup.objects.get(group = 1))
        return gsuser


# class Site(models.Model):
#     db_server = models.CharField(max_length=15)
#     gis_server = models.CharField(max_length=15)
#     db_instance = models.CharField(max_length=15)
#     sde_instance = models.CharField(max_length=15)
#     map_instance = models.CharField(max_length=15)
#     grid_instance = models.CharField(max_length=15)
#     username = models.CharField(max_length=15)
#     caps = models.CharField(max_length=15)
#     caps2 = models.CharField(max_length=15)
#     caps2 = models.CharField(max_length=15)

# // loads in variables
# 		var remoteConf = {
# 		    capabilities: {},
# 			dbServer: "{{ instance.db_server }}",
# 			gisServer: "{{ instance.gis_server }}",
# 			dbInstance: "{{ instance.db_instance }}",
# 			sdeInstance: "{{ instance.sde_instance }}",
# 			sdePfx: "{{ instance.sde_pfx }}",
# 			mapInstance: "{{ instance.map_instance }}",
# 			gridInstance: "{{ instance.grid_instance }}",
# 			user: "{{ user.username }}",
# 			caps: "{{caps}}",
# 			caps2: "{{capabilities}}",
# 			staticRoot: "{% static 'gs/' %}"

