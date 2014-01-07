__author__ = 'Wayne'
import api_connection as api
from models import Match, World


def get_worlds():
    """
    http://wiki.guildwars2.com/wiki/API:1/world_names
    """
    for w in api.api_request('world_names'):
        world = World(world_id=w['id'], name=w['name'])
        world.save()

    return World.objects.all()


def get_matches():
    """
    http://wiki.guildwars2.com/wiki/API:1/wvw/matches
    """
    for m in api.api_request('wvw/matches')['wvw_matches']:
        match = Match(
            match_id=m['wvw_match_id'],
            red=World.objects.get(world_id=m['red_world_id']),
            blue=World.objects.get(world_id=m['blue_world_id']),
            green=World.objects.get(world_id=m['green_world_id']),
            start_time=m['start_time'],
            end_time=m['end_time'])
        match.save()

    return Match.objects.all()