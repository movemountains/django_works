from django.shortcuts import render


def bucket_home(request):
    return render(request, '/bucket.html')

