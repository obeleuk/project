from django.shortcuts import render
from django import forms

from . import util



class savepage(forms.Form):
    title=forms.CharField(label="Title")
    body = forms.CharField(widget=forms.Textarea(attrs={'name':'Body', 'style':'height:20em;'}))




class editpage(forms.Form):
    title = forms.CharField(label="Title")
    body = forms.CharField(widget=forms.Textarea(attrs={'name':'Body', 'style':'height:20em;'}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create(request):
    
    return render(request, "encyclopedia/create.html", {"form":savepage()
                                                        })


def edit(request):
    return render(request, "encyclopedia/edit.html",  {"form1":editpage()
                                                        })


