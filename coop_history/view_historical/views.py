from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
import dataAccess


# Create your views here.
def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


def loadAjaxData(request, query):
    if query == 'getStudent':
        students = dataAccess.getStudentDT()
        return render_to_response('studentDT.html', {'students': students}, context_instance=RequestContext(request))
    return HttpResponse(query)