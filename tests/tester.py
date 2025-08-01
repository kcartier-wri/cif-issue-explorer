from src.timezonefinder_code import get_tz_name


def test_tzf():
    center_lon = -122.2
    center_lat = 47.6
    tz_name = get_tz_name(center_lon, center_lat)

    assert tz_name == 'America/Los_Angeles'

