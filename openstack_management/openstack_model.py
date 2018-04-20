from django.db import models
from django.conf import settings

class OpenStackPlatform(models.Model):
    endpoint =   models.CharField()
    username =   models.CharField()
    password =   models.CharField()
    openstack_name = models.CharField()
    last_validated = models.DateField()

class OpenStackData(models.Model):
    DATASTATUS = (
        (RUNNING,"running"),
        (SHUTDOWN,"shutdown"),
        (PAUSE,"pause"),
    )
    description = models.TextField(null=True)
    ops = models.ForeignKey(OpenStackPlatform, on_delete=models.CASCADE)
    uuid = models.UUIDField()
    name = models.CharField(null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    ) #(bfp user)
    created = models.DateField()
    updated = models.DateField()    
    status = models.CharField(choices=DATASTATUS)
    project_id = models.CharField()
    archived = models.BooleanField(default=False)
    #Add tag ?

    class Meta:
        abstract = True

class Properties(models.Model):
    """
    Openstack create resource properties.
    ex. openstack volume create avolume type="ceph"
    ceph is type property
    ???
    """
class Projects(OpenStackData):
    uuid = models.CharField()
    domain_id = models.CharField()
    enabled = models.BooleanField()

class Vms(OpenStackData):
    uptime = models.DateField()#(last update - latest update)
    key_name = models.CharField() #(keypair_name)
    error = models.IntegerField() #(error count)
    flavor_name = models.CharField()
    flavor_id = models.CharField()
    host_id = models.UUIDField()
    
    def uptime(self,new_date):
        days = now() - self.created
        return days.day

    @property
    def get_security_groups(self):
        security_model.objects.filter(vm=self.uuid)

class VmsSecurityGroup(models.Model):
    vm = models.ForeignKey(Vms)
     
    

class Volumes(OpenStackData):
    size
    volume_type 

class Containers(OpenStackData):
    openstack
    uuid

class MonitorData(OpenStackData):
    openstack
    uuid

class Networks(OpenStackData):
    cidr

class Subnets(OpenStackData):
    cidr = models.CharField()
    gateway_ip = 
    

class Ports(OpenStackData):
    subnet = models.ForeignKey(Subnets)
    ip_address = models.GenericIPAddressField()


class SecurityGroups(OpenStackData):
    """
   
    """
    @property
    def rules(self):
        retrun self.securitygrouprule_set()

class SecurityGroupRules(OpenStackData):
    security_group_id = models.ForeignKey(SecurityGroups,on_delete=CASCADE)
    protocol = models.CharField()



