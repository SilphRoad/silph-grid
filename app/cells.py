
from aiohttp import web
from s2sphere import (
    Cell,
    Point,
    LatLng,
)


async def from_latlng(req):
    """
    ---
    summary: S2 Cells
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
    cell = Cell.from_lat_lng(p)
    if zoom < 30:
        cell = Cell(cell.id().parent(zoom))

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
