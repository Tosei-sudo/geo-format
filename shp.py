import json

from cls.dummy import File
from cls.geometry import GeometryFileFormat

from format.dBase4 import dBase4
from format.geojson import GeoJson
from format.Shapefile import Shapefile
from format.ShapeIndex import ShapeIndex

path = "sample/shp/dted-mesh/G04-a-11_5340-jgd_ElevationAndSlopeAngleTertiaryMesh"

with open(path + '.shp', 'rb') as f:
    shp_file = File(f.read())

with open(path + '.shx', 'rb') as f:
    shx_file = File(f.read())

with open(path + '.dbf', 'rb') as f:
    dbf_file = File(f.read())

dbf = dBase4()
dbf.read(dbf_file)

shp = Shapefile()
shp.read(shp_file)

shx = ShapeIndex()
shx.read(shx_file)
print shp.header.__dict__

geometrys = []
for record in shp.records:
    geometrys.append(record.geometry)

shp2 = Shapefile()
shp2.create(geometrys)

with open(path + '-copy.shp', 'wb') as f:
    f.write(shp2.export())

shx = ShapeIndex()
shx.create(shp)

with open(path + '-copy.shx', 'wb') as f:
    f.write(shx.export())

with open(path + '-copy.prj', 'w') as f:
    f.write(shp.get_prj())

with open(path + '-copy.dbf', 'wb') as f:
    f.write(dbf.export())

geojson = GeoJson([])

properties_list = []
for index, record in enumerate(shp.records):
    properties = dbf.records[index].__dict__
    geojson.add_feature(record.geometry.export(GeometryFileFormat.GEOJSON), properties, record.geometry.TYPE_NAME)
    properties_list.append(properties)

with open('sample/geojson/jgd_ElevationAndSlopeAngleTertiaryMesh.geojson', 'w') as f:
    f.write(json.dumps(geojson.get_dict()))

t = dBase4()
t.create(properties_list)

with open('sample/dbf/test.dbf', 'wb') as f:
    f.write(t.export())