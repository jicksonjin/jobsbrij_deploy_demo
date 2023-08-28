from django import forms
from ckeditor.widgets import CKEditorWidget  # Import CKEditorWidget
from . models import *
class JobDetailsForm(forms.ModelForm):
    class Meta:
        model = job_details  # Assuming 'job_details' is your model
        fields = ['company_name', 'job_title', 'expiry_on', 'job_description', 'how_to_apply', 'cat', 'image']

    # Use CKEditorWidget for the rich text fields
    job_description = forms.CharField(widget=CKEditorWidget())
    how_to_apply = forms.CharField(widget=CKEditorWidget())
