"""Autograding script."""

import os


def test_01():
    """Test word count job."""

    assert os.path.exists("Files/output/summary.csv")
    assert os.path.exists("Files/plots/top10_drivers.png")
