
from s2sphere import (
    Cell as s2Cell,
    CellId,
    LatLng,
    Point,
)


class Cell(object):
    __s2cell = None

    def __init__(self, id):
        self.__s2cell = s2Cell(id)

    @classmethod
    def from_token(cls, token):
        return cls(CellId.from_token(token))

    @classmethod
    def from_latlng(cls, lat, lng, zoom=30):
        p = LatLng.from_degrees(lat, lon)
        cell = CellId.from_lat_lng(p)
        if zoom < 30:
            cell = cell.parent(zoom)

        return cls(cell)

    def from_point(point, zoom=30):
        pass

    def __repr__(self):
        return self.token

    @property
    def id(self):
        return self.__s2cell.id().id()

    @property
    def token(self):
        return self.__s2cell.id().to_token()

    @property
    def level(self):
        return self.__s2cell.level()

    @property
    def center(self):
        return self.__s2cell.get_center()

    @property
    def vertices(self):
        v = [LatLng.from_point(self.__s2cell.get_vertex(i)) for i in range(4)]
        return [[l.lat().degrees, l.lng().degrees] for l in v]

    @property
    def struct(self):
        return {
            'id': self.id,
            'token': self.token,
            'level': self.level,
            'vertices': self.vertices,
        }

