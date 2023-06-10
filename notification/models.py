from django.db import models

# Create your models here.
class Notification(models.Model):
    notificationid = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    message = models.CharField(max_length=1000)
    isread = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "notification"
        ordering = ["-created_at"]

    def __str__(self):
        return self.message

    def get_notification(self):
        return self.message

