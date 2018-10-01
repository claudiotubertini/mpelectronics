from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    # def clean_form(self):
    #     data = self.cleaned_data['renewal_date']
    #
    #     # Check date is not in past.
    #     if data < datetime.date.today():
    #         raise ValidationError(_('Invalid date - renewal in past'))
    #
    #     # Check date is in range librarian allowed to change (+4 weeks).
    #     if data > datetime.date.today() + datetime.timedelta(weeks=4):
    #         raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
    #
    #     # Remember to always return the cleaned data.
    #     return data

