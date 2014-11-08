from django import forms

from .models import Bucket_list

class BucketForm(forms.ModelForm):
    class Meta:
        model = Bucket_list
