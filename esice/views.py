from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    template_name = 'google_verification.html'

    return render(
        request,
        template_name,
        {}
    )
