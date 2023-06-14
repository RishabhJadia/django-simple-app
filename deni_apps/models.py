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
