#!/usr/bin/env python

import collections


def IterStopPoints(stopPoints):
    '''
"$type": "Tfl.Api.Presentation.Entities.Identifier, Tfl.Api.Presentation.Entities", 
"uri": "/StopPoint/940GZZLUESQ", 
"type": "StopPoint", 
"id": "940GZZLUESQ", 
"name": "Euston Square Underground Station"
    '''
    for m in stopPoints:
        yield (m["id"], m["name"])


def _GetJourneyResultN(j):
    # dt - seems to be ISO8601 - yyyy-mm-ddTHH:MM:SS with times in UTC
    #      where T is just the character 'T'
    dt_start = j["startDateTime"]
    dt_arrive = j["arrivalDateTime"]
    rv =collections.OrderedDict()
    rv["start"] = dt_start
    rv["arrival"]= dt_arrive
    #rv["legs"] = j["legs"]
    sp = j["legs"][0]["path"]["stopPoints"]
    rv["stopPoints"] = [ (x,y) for x,y in IterStopPoints(sp) ]
    return rv


def GetJourneyResult(the_dict, n):
    rv = list()
    for x in the_dict["journeys"]:
        rv.append( _GetJourneyResultN(x) )
    return rv
