import json

from cls.converter import ShapePackage, shapepackage2geojson, geojson2shapepackage

path = "sample/shp/N02-22_RailroadSection/N02-22_RailroadSection"

pack = ShapePackage()
pack.read(path)
# print hashlib.md5(pack.shx.records.export()).hexdigest()

geojson = shapepackage2geojson(pack)
with open('sample/geojson/export.geojson', 'w') as f:
    f.write(json.dumps(geojson.get_dict()))

export_pack = geojson2shapepackage(geojson)
export_pack.save('sample/shp/export', True)

geojson2 = shapepackage2geojson(export_pack)
with open('sample/geojson/export2.geojson', 'w') as f:
    f.write(json.dumps(geojson2.get_dict()))