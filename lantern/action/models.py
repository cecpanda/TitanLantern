from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


UserModel = get_user_model()


class Action(models.Model):
    user = models.ForeignKey(UserModel, related_name='actions', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj', on_delete=models.SET_NULL)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_ct', 'target_id')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user.username} {self.verb} {self.target}'
        