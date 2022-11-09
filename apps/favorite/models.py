from django.db import models

# Create your models here.


from django.db import models
from apps.users.models import User
from apps.items.models import Item

class Favorite(models.Model):
    class Meta:
        db_table = 'favorite'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True
    )
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, db_index=True
    )
    like = models.CharField(
        'favorite', max_length=5, blank=False, null=False, db_index=True
    )
    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )

    