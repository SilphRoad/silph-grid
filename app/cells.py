
from aiohttp import web
from s2sphere import (
    Cell as s2Cell,
    Point,
    LatLng,
    LatLngRect,
    RegionCoverer,
)

from model.cell import Cell


async def from_rect(req):
    """
    ---
    summary: S2 Cells in a rect
    description: Given a set of lat/lng and zoom, produce cell(s)
    tags:
    - Cells
    parameters:
    - name: p0[lat]
      in: query
      description: Latitude component of top left corner of rect
      type: number
      required: true
    - name: p0[lng]
      in: query
      description: Longitude component of top left corner of rect
      type: number
      required: true
    - name: p1[lat]
      in: query
      description: Latitude component of bottom right corner of rect
      type: number
      required: true
    - name: p1[lng]
      in: query
      description: Longitude component of bottom right corner of rect
      type: number
      required: true
    - name: zoom
      in: query
      description: Zoom level of location
      type: number
      required: false
      default: 16
    produces:
    - text/json
    responses:
      "200":
        description: successful operation
      "400":
        description: invalid parameters
    """

    p1_lat = float(req.query['p0[lat]'])
    p2_lat = float(req.query['p1[lat]'])
    p1_lng = float(req.query['p0[lng]'])
    p2_lng = float(req.query['p1[lng]'])

    zoom = int(req.query.get('zoom', 16))

    r = RegionCoverer()
    r.max_level = zoom
    r.min_level = zoom

    p1 = LatLng.from_degrees(p1_lat, p1_lng)
    p2 = LatLng.from_degrees(p2_lat, p2_lng)

    ids = r.get_covering(LatLngRect.from_point_pair(p1, p2))
    cell_ids = [Cell(id) for id in ids]

    return web.json_response({k.token: k.struct for k in cell_ids})


async def from_latlng(req):
    """
    ---
    summary: S2 Cell @ Latitude / Longitude
    description: Given a lat/lng and optional zoom, produce a Cell
    tags:
    - Cells
    parameters:
    - name: latitude
      in: formData
      description: Latitude component of location
      type: number
      required: true
    - name: longitude
      in: formData
      description: Longitude component of location
      type: number
      required: true
    - name: zoom
      in: formData
      description: Zoom level of location
      type: number
      required: false
      default: 30
    produces:
    - text/html
    responses:
        "200":
            description: successful operation. Returns "Cell" obj
        default:
            description: invalid operation. Input variables provided did not produce valid result
    """

    data = await req.post()
    lat = float(data['latitude'])
    lon = float(data['longitude'])
    zoom = int(data.get('zoom', 30))

    p = LatLng.from_degrees(lat, lon)
    cell = s2Cell.from_lat_lng(p)
    if zoom < 30:
        cell = s2Cell(cell.id().parent(zoom))

    return web.json_response({'id': cell.id().to_token()})


async def cellid(req):
    """
    ---
    summary: S2 Cell Data
    description: Given a Cell ID, produce cell data
    tags:
    - Cells
    parameters:
    - name: id
      in: path
      description: Cell ID
      type: string
      required: true
    produces:
    - text/html
    responses:
        "200":
            description: successful operation. Returns "Cell" obj
        default:
            description: invalid operation. Input variables provided did not produce valid result
    """
    with open('views/index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')
