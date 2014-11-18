from django import forms


class BucketForm(forms.ModelForm):
    class Meta:
        model = Bucket
        fields =("")
