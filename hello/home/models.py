from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)  # Use EmailField
    phone = models.CharField(max_length=50)
    
    
    CONTACT_REASONS = [
        ('1', 'General Inquiry'),
        ('2', 'Feedback'),
        ('3', 'Support'),
    ]
    contact_reason = models.CharField(
        max_length=1,
        choices=CONTACT_REASONS,
        default='1',  # default can be set to 'General Inquiry'
    )

    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fullname
    


