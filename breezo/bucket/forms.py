from django import forms
from .models import BucketList,To_Do,Done,Doing

class BucketListForm(forms.ModelForm):
    class Meta:
        model = BucketList

class To_DoForm(forms.ModelForm):
    class Meta:
        model = To_Do

class DoneForm(forms.ModelForm):
    class Meta:
        model = Done


class DoingForm(forms.ModelForm):
    class Meta:
        model = Doing


