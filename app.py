
from aiohttp import web
from aiohttp_swagger import setup_swagger

from app import (
    cells,
)

from s2sphere import (
    Cell,
    LatLng,
)


async def index(req):
    """
    ---
    description: This end-point produces a simple example webpage.
    produces:
    - text/html
    responses:
        "200":
            description: successful operation. Return "welcome" text
    """
    with open('views/index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_post('/cell', cells.from_latlng)
    app.router.add_get('/cell/{id}', cells.cellid)

    setup_swagger(app, swagger_url='/api/v0/doc')

    web.run_app(app, port=8081)
