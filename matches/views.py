from django.shortcuts import render_to_response
from django.template.context import RequestContext
from gw2api.wvw_requests import get_match_details

def match(request, server_group, match_number):
    output = dict({})
    match_id = server_group + "-" + match_number

    output['title'] = "Match Details for %s" % match_id
    output['content'] = get_match_details(match_id)

    return render_to_response('base.html', output, context_instance=RequestContext(request))