from timezonefinder import TimezoneFinder



def get_tz_name(center_lon, center_lat):
    # Initialize TimezoneFinder
    tf = TimezoneFinder()
    # Find the timezone of the center point
    tz_name = tf.timezone_at(lng=center_lon, lat=center_lat)

    return tz_name