# Import django modules
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.gis.geos import Point
from django.contrib.gis.gdal import DataSource
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
# Import system modules
import simplejson
import itertools
import tempfile
import os
# Import custom modules
from waypoints.models import Waypoint


def index(request):
    'Display map'
    waypoints = Waypoint.objects.order_by('name')
    c = {
        'waypoints': waypoints,
        'content': render_to_string('waypoints/waypoints.html', {'waypoints': waypoints}),
    }
    c.update(csrf(request))
    return render_to_response('waypoints/index.html', c)


def save(request):
    'Save waypoints'
    for waypointString in request.POST.get('waypointsPayload', '').splitlines():
        waypointID, waypointX, waypointY = waypointString.split()
        waypoint = Waypoint.objects.get(id=int(waypointID))
        waypoint.geometry.set_x(float(waypointX))
        waypoint.geometry.set_y(float(waypointY))
        waypoint.save()
    return HttpResponse(simplejson.dumps(dict(isOk=1)), content_type='application/json')


def search(request):
    'Search waypoints'
    # Build searchPoint
    try:
        searchPoint = Point(float(request.GET.get('lng')), float(request.GET.get('lat')))
    except:
        return HttpResponse(simplejson.dumps(dict(isOk=0, message='Could not parse search point')))
    # Search database
    waypoints = Waypoint.objects.distance(searchPoint).order_by('distance')
    # Return
    return HttpResponse(simplejson.dumps(dict(
        isOk=1,
        content=render_to_string('waypoints/waypoints.html', {
            'waypoints': waypoints
        }),
        waypointByID=dict((x.id, {
            'name': x.name,
            'lat': x.geometry.y,
            'lng': x.geometry.x,
        }) for x in waypoints),
    )), content_type='application/json')


def upload(request):
    'Upload waypoints'
    # If the form contains an upload,
    if 'gpx' in request.FILES:
        # Get
        gpxFile = request.FILES['gpx']
        # Save
        targetPath = tempfile.mkstemp()[1]
        destination = open(targetPath, 'wt')
        for chunk in gpxFile.chunks():
            destination.write(chunk)
        destination.close()
        # Parse
        dataSource = DataSource(targetPath)
        layer = dataSource[0]
        waypointNames = layer.get_fields('name')
        waypointGeometries = layer.get_geoms()
        for waypointName, waypointGeometry in itertools.izip(waypointNames, waypointGeometries):
            waypoint = Waypoint(name=waypointName, geometry=waypointGeometry.wkt)
            waypoint.save()
        # Clean up
        os.remove(targetPath)
    # Redirect
    return HttpResponseRedirect(reverse('waypoints-index'))