import geopandas as gpd
from shapely.geometry import Polygon
import s2sphere

def s2_latlng_to_polygon(latlng,parent_level=7):
    cell = s2sphere.Cell.from_lat_lng(s2sphere.LatLng.from_degrees(*latlng))
    parent_cell = s2sphere.Cell(cell.id().parent(parent_level))
    polygon_tuples = [
        (float(x[1]),float(x[0])) for x in [
            str(s2sphere.LatLng.from_point(parent_cell.get_vertex(k))).replace('LatLng: ','').split(',') for k in range(4)
        ]
    ]
    return polygon_tuples