import json

from cls.geometry import Point, GeometryFileFormat, Polygon, Polyline

from format.dBase4 import dBase4


from format.geojson import GeoJson

geojson = GeoJson([])

points = [
    [125, 36],
    [125, 37],
    [124, 37],
    [124, 36],
    [125, 36]
]

rings = []
for point in points:
    p = Point()
    p.create(point[0], point[1])
    rings.append(p)

line = Polyline()
line.create(rings)
geojson.add_feature(line.export(GeometryFileFormat.GEOJSON), {}, line.TYPE_NAME)

with open('sample/geojson/test.geojson', 'w') as f:
    f.write(json.dumps(geojson.get_dict()))