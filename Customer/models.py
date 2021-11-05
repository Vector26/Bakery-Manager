import uuid
from django.db import models
from django.contrib.auth.models import User
from bakery.models import *
# Create your models here.
class order_history(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.OneToOneField(User,related_name='User',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class orders(models.Model):
    productKey=models.ForeignKey(product,related_name="productKey",on_delete=models.CASCADE)
    freq=models.IntegerField()
    order_id=models.ForeignKey(order_history,related_name="order_history",on_delete=models.CASCADE)
    date=models.DateTimeField(auto_created=True,auto_now_add=True)

    def __str__(self):
        return str(self.productKey)+" on "+str(self.date)

