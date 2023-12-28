from django.db import models
from django.conf import settings
from OrderApp.models import Order
from ShopingApp.models import Product
# Create your models here.

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=264, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.user.user_info.username} billing address'

    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]

        for field_name in field_names:
            value = getattr(self, field_name)
            if value is None or value=='':
                return False
        return True

    class Meta:
        verbose_name_plural = "Billing Addresses"




class OrderMsg(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    driscribe_your_customize = models.TextField(blank=True, null=True)
    Attach_image = models.ImageField(upload_to='order', blank=True, null=True  )
    provid_any_link = models.URLField(blank=True, null=True)
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    is_creat = models.BooleanField(default=False)
    item= models.ForeignKey(Product, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.driscribe_your_customize} messages'


    class Meta:
        verbose_name_plural = "tex msg"