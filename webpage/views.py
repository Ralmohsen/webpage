# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def index(request, parameter=None):
    context = {
        "link_to_CV": "/static/CV.pdf",
        "parameter": parameter
    }
    return render(request, 'index.html', context)
