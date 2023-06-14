from django.db import models

# from simple_history.models import HistoricalRecords

# NAME, JOINIG DATE, EMAIL_ID, HIRING MANAGER, MANAGER EMAIL_ID


# Create your models here.
class Nameable(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class CandidateDetails(Nameable):
    name = models.CharField('Name', max_length=100)
    candiate_doj = models.DateField('Candidate Joining Date', default=None)
    offer_accepted_date = models.DateField("Offer Accepted Date", default=None)
    email_sent_date = models.DateField("Email Sent Date", default=None)
    candiate_email_id = models.EmailField('Candidate Email Id', max_length=50,)
    hiring_manager = models.CharField('Hiring Manager', max_length=100)
    hiring_manager_email_id = models.EmailField('Hiring Manager Email Id', max_length=50,)
    # history = HistoricalRecords()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Candidate Details'


# from django.core.mail import send_mail
# from django.conf import settings
# from django.db import models

# class MyModel(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField()

#     def save(self, *args, **kwargs):
#         """
#         Override the save method to send an email when the age field is set to 30 and saved.
#         """
#         if self.pk is None and self.age == 30: # Check if the instance is being created and the age field is 30
#             subject = 'Age of {} is now 30!'.format(self.name)
#             message = 'The age of {} ({}) is now 30!'.format(self.name, self.email)
#             from_email = settings.DEFAULT_FROM_EMAIL
#             recipient_list = ['recipient@example.com']
#             send_mail(subject, message, from_email, recipient_list)

#         super().save(*args, **kwargs)

# # In your view, when the user clicks the save button:
# my_model_instance = MyModel(name='John Doe', age=30, email='example@example.com')
# my_model_instance.save()



# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings
# from .models import MyModel

# @receiver(post_save, sender=MyModel)
# def send_email_on_save(sender, instance, **kwargs):
#     """
#     Signal receiver function to send an email when the age field is set to 30 and saved.
#     """
#     if instance.age == 30:
#         subject = 'Age of {} is now 30!'.format(instance.name)
#         message = 'The age of {} ({}) is now 30!'.format(instance.name, instance.email)
#         from_email = settings.DEFAULT_FROM_EMAIL
#         recipient_list = ['recipient@example.com']
#         send_mail(subject, message, from_email, recipient_list)

# # In your view, when the user clicks the save button:
# my_model_instance = MyModel(name='John Doe', age=30, email='example@example.com')
# my_model_instance.save()