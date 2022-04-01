#!/usr/bin/env python

"""Tests for `invasive_checker` package."""

import pytest
from invasive_checker import invasive_checker
import warnings
from shapely.errors import ShapelyDeprecationWarning
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning)

def test_invasive():
    """Sample pytest test function with the pytest fixture as an argument."""

    warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning)
    lon = 2.5
    lat = 51.5
    aphia_id = 132818

    aphia_checker = invasive_checker.Aphia_Checker()
    aa, bb = aphia_checker.check_aphia(lon, lat, aphia_id)

    assert aa['aphia_id']==132818
    assert aa['distance [km] to nearest introduced location']==0.0
    assert aa['nearest introduced MRGID'] == [21912]

def test_native():
    """Sample pytest test function with the pytest fixture as an argument."""

    warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning)
    lon = 2.5
    lat = 51.5
    aphia_id = 126436
    aphia_checker = invasive_checker.Aphia_Checker()
    aa, bb = aphia_checker.check_aphia(lon, lat, aphia_id)

    assert aa['aphia_id']==126436
    assert aa['sample location within <buffer> of aphia distribution']
    assert aa['distance [deg] to nearest introduced location'] == "No known 'introduced' locations"
