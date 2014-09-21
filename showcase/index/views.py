from django.shortcuts import redirect, render_to_response, get_object_or_404, render
# from django.template import RequestContext
from django.core.urlresolvers import reverse


def home(request):
    return render(request, 'index/home.html')