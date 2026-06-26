from geopy.geocoders import Nominatim

class LocationAgent:

    def get_safe_locations(self, location_name):

        geolocator = Nominatim(user_agent="project_sentinel")

        safe_places = [
            "Government Hospital",
            "Government School",
            "Community Hall",
            "Sports Stadium"
        ]

        locations = []

        for place in safe_places:

            try:
                query = f"{place}, {location_name}"

                loc = geolocator.geocode(query)

                if loc:

                    locations.append({
                        "name": place,
                        "latitude": loc.latitude,
                        "longitude": loc.longitude,
                        "maps_url":
                            f"https://www.google.com/maps/search/?api=1&query={loc.latitude},{loc.longitude}"
                    })

            except:
                pass

        return locations