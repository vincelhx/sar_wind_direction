# Function copied from xsarsea library
import numpy as np


def dir_meteo_to_sample(meteo_dir, ground_heading):
    """
    Convert meteorological N/S direction to image convention

    Parameters
    ----------
    meteo_dir: meteorological direction in degrees north
    ground_heading: azimuth at position, in degrees north

    Returns
    -------
    np.float64
        same shape as input. angle in radian, relative to sample, anticlockwise
    """

    return np.pi / 2 - np.deg2rad(meteo_dir - ground_heading)


def dir_sample_to_meteo(sample_dir, ground_heading):
    """
    Convert image direction relative to antenna to meteorological direction

    Parameters
    ----------
    sample_dir: angle in degrees, relative to sample, anticlockwise
    ground_heading: azimuth at position, in degrees north

    Returns
    -------
    np.float64
        same shape as input. meteorological direction in degrees north
    """

    return 90 - sample_dir + ground_heading


def dir_meteo_to_oceano(meteo_dir):
    """
    Convert meteorological direction to oceanographic direction

    Parameters
    ----------
    meteo_dir: float
        Wind direction in meteorological convention (clockwise, from), ex: 0°=from north, 90°=from east

    Returns
    -------
    float
        Wind direction in oceanographic convention (clockwise, to), ex: 0°=to north, 90°=to east
    """
    oceano_dir = (meteo_dir + 180) % 360
    return oceano_dir


def dir_oceano_to_meteo(oceano_dir):
    """
    Convert oceanographic direction to meteorological direction

    Parameters
    ----------
    oceano_dir: float
        Wind direction in oceanographic convention (clockwise, to), ex: 0°=to north, 90°=to east

    Returns
    -------
    float
        Wind direction in meteorological convention (clockwise, from), ex: 0°=from north, 90°=from east
    """
    meteo_dir = (oceano_dir - 180) % 360
    return meteo_dir


def dir_to_180(angle):
    """
    Convert angle to [-180;180]

    Parameters
    ----------
    angle: float
        angle in degrees

    Returns
    -------
    float
        angle in degrees
    """
    angle_180 = (angle + 180) % 360 - 180
    return angle_180


def dir_to_360(angle):
    """
    Convert angle to [0;360]

    Parameters
    ----------
    angle: float
        angle in degrees

    Returns
    -------
    float
        angle in degrees
    """
    angle_360 = (angle + 360) % 360
    return angle_360
