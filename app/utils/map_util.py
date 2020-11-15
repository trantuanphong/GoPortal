import json

class MapboxUtil:

    def toGeoJSON(clubs):
        features = []
        for club in clubs:
            feature = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [club.lng, club.lat]
                },
                'properties': {
                    'description': club.dumpHTML()
                }
            }
            features.append(feature)
        geojson = {
            'type': 'geojson',
            'data': {
                'type': 'FeatureCollection',
                'features': features
            }
        }
        geojson = json.dumps(geojson)
        return geojson