from django.shortcuts import redirect, render_to_response, get_object_or_404, render
# from django.template import RequestContext
from django.core.urlresolvers import reverse
from utils.bash_commands import command_entry
from forms import CommandForm


def home(request):
    result = ""
    form = CommandForm()
    if request.POST or None:
        form = CommandForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data['entry']
            result = command_entry(entry)

    return render(request,
                  'index/home.html',
                  {'form':form,
                   'result':result})