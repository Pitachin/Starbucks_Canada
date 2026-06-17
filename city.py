import config

# Generate dense coordinate grids around major Canadian cities
# API's limit is 50 store in dense urban areas.

def make_grid(center_lat, center_lng, radius = 0.4, step = 0.02):
    """Generate a grid of coordinates around a city center.

    Args:
        center_lat, center_lng: city center coordinates
        radius: how for to extend from center
        step: spacing between each grid points

    Returns:
        list of (lat, lng) tuples covering the area
    """
    points = []
    lat = center_lat - radius
    while lat <= center_lat + radius:
        lng = center_lng - radius
        while lng <= center_lng + radius:
            points.append((round(lat, 4), round(lng, 4)))
            lng += step
        lat += step
    return points

def build_city_grids():
    """Build a combined list of dense grid coordinates for all major cities."""
    coords = []
    for city in config.MEGA_CITIES:
        coords += make_grid(*city, radius=0.3, step=0.02)    # finer
    for city in config.BIG_CITIES:
        coords += make_grid(*city, radius=0.25, step=0.04)   # medium
    return coords

if __name__ == "__main__":
    grids = build_city_grids()
    print(f"Total city-grid points: {len(grids)}")

