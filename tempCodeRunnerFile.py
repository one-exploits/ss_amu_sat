def calculate_gps_from_pixel(center_gps, spatial_factor, pixel_displacement):
    center_lat, center_lon = center_gps
    lat_per_pixel = spatial_factor * 0.00001  # Adjust the spatial factor as needed
    lon_per_pixel = spatial_factor * 0.00002  # Adjust the spatial factor as needed

    displacement_x, displacement_y = pixel_displacement

    new_lat = center_lat + displacement_y * lat_per_pixel
    new_lon = center_lon + displacement_x * lon_per_pixel

    return new_lat, new_lon
