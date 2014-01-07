from django.shortcuts import render_to_response
from django.template.context import RequestContext
from gw2api.wvw_requests import get_worlds, get_matches


def home(request):

    output = dict({})
    output['title'] = "GW2 Commander Tools"
    # output['content'] = "Worlds: <br />"
    # for world in get_worlds().iterator():
    #     output['content'] += "name: %s <br />" % world.name

    output['content'] = "Matches: <br />"
    for match in get_matches().iterator():
        output['content'] += "match id: {id}, red: {red}, blue: {blue}, green: {green} <br />"\
            .format(id=match.match_id, red=match.red, blue=match.blue, green=match.green)


    return render_to_response('base.html', output, context_instance=RequestContext(request))