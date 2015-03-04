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
    elif query == 'getCompany':
        companies = dataAccess.getCompanyDT()
        return render_to_response('companyDT.html', {'companies': companies}, context_instance=RequestContext(request))
    elif query == 'getContact':
        contacts = dataAccess.getContactDT()
        return render_to_response('contactDT.html', {'contacts': contacts}, context_instance=RequestContext(request))
    elif query == 'getPlacement':
        placements = dataAccess.getPlacementDT()
        return render_to_response('placementDT.html', {'placements': placements}, context_instance=RequestContext(request))
    else:
        return HttpResponse("invalid ajax request")
