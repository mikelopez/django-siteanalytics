from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.simple import redirect_to
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest, Http404, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse, resolve
from django.template import RequestContext, loader, Context
from datetime import datetime

import random
import simplejson
import logging

try:
    from settings import LOG_ON
except ImportError:
    LOG_ON = False


def raise_json(data):
    """ 
        return JSON response 
    """
    return HttpResponse(simplejson.dumps(data), mimetype="application/json")

def robots(request):
    """ 
        Return robots response
    """
    return HttpResponse('User-agent: *', mimetype="text/plain")

def test_index(request, linkname=None, filtername=None):
    """
        Index View
        Set the logger instance
        -----
        optional linkname: sitename.com/linkname - loads website page with name "linkname"
        optional filtername: sitename.com/landing/12 - landing page ID 12
    """

    return render_to_response('django_siteanalytics/test-index.html', {}, RequestContext(request))
# Create your views here.
