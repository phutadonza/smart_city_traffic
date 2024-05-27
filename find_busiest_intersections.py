def find_busiest_intersections(intersections):
    """
    Find the intersections with the highest number of vehicles.
    
    Parameters:
    intersections (dict): A dictionary where keys are intersection names and values are the number of vehicles.
    
    Returns:
    list: A list of intersection names with the highest number of vehicles.
    """
    if not intersections:
        return []

    max_vehicles = max(intersections.values())
    busiest_intersections = [name for name, count in intersections.items() if count == max_vehicles]
    
    return busiest_intersections
