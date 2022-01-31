from django.db import models
from account.models import User
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

# Create your models here.
class Query(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name = 'mentor')
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name = 'student')
    query = models.TextField(null=True,blank=True)
    response = models.TextField(null=True,blank=True)
    answered = models.BooleanField(_('Answered'), default=False)
    document = FilerFileField(related_name='document',
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL
                                   )
    created_on = models.DateTimeField(_('Created Date'), auto_now_add=True)
    updated_on = models.DateTimeField(_('Updated Date'), auto_now=True)

    def __str__(self):
        return self.query

    class Meta:
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'
