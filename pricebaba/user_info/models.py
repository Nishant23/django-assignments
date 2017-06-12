from __future__ import unicode_literals

from django.db import models

class users(models.Model):
    first_name = models.CharField(max_length = 25, help_text  = "First Name")
    last_name = models.CharField(max_length = 40, help_text = 'Last Name')
    email_id = models.CharField(max_length = 100, help_text = 'Email Id')
    mobile = models.CharField(max_length = 10, help_text = 'Mobile Number')
    age = models.CharField(max_length = 3, help_text = 'Age')
    date_of_birth = models.CharField(max_length = 30, help_text = "dob")
    place = models.CharField(max_length = 1000, help_text = "Place")

    class Meta:
        ordering = ["first_name", "last_name"]

    def get_absolute_url(self):
        return reverse('edit', args=[str(self.id)])

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
