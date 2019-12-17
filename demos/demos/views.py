from django.shortcuts import render
from . import forms
from django.template.context_processors import csrf


def dropdemo(request):
    if request.method == 'POST':
        c = {
            'base64text': request.POST["areaone"],
        }
    else:
        form = forms.UserForm(label_suffix='：')
        c = {'form': form}
        c.update(csrf(request))
    return render(request, 'dragdrop.html', c)


def freedraw(request):
    if request.method == 'POST':
        c = {
            'base64text': request.POST["areaone"],
        }
    else:
        form = forms.UserForm(label_suffix='：')
        c = {'form': form}
        c.update(csrf(request))
    return render(request, 'canvas01.html', c)
