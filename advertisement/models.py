from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='advertisement/', null=True)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'advertisements'
        
    def __str__(self):
        return str(self.added)
