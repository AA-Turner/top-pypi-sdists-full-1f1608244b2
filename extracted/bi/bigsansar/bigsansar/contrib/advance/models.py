from django.db import models
from bigsansar.contrib.sites.models import domains
from django.contrib.auth.models import User

# Create your models here.


from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class admin_update(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField(default='bigsansar.com/dashboard',)
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'update'
        verbose_name_plural = 'Admin Update'



class SidebarSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_sidebar_open = models.BooleanField(default=True)  # Boolean field to control sidebar visibility

    def __str__(self):
        return "Sidebar Settings"
    


class cloudflare_api(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    global_api_key = models.CharField(max_length=500)
    email = models.EmailField()
    main_domain_name = models.CharField(max_length=100)
    account_id = models.CharField(max_length=500)
    ip_address = models.GenericIPAddressField(default='127.0.0.1')
    ip_address2 = models.GenericIPAddressField(default='127.0.0.2')