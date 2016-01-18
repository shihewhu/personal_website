from django.forms import ModelForm, Textarea
from blog.models import Contact_information
from django.utils.translation import ugettext_lazy as _

class ContactForm(ModelForm):
    class Meta:
        model = Contact_information
        fields = '__all__'
        labels = {
            'name': _('Name'),
            'email': _('Email'),
            'phone_number': _('Phone Number'),
            'message': _('Message'),
        }
        widgets = {
            'name': Textarea(attrs={'cols': 60, 'rows': 1}),
            'email': Textarea(attrs={'cols': 60, 'rows': 1}),
            'phone_number': Textarea(attrs={'cols': 60, 'rows': 1}),
            'message': Textarea(attrs={'cols': 60, 'rows': 4}),

        }

