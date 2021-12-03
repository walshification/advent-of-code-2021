"""
Part One
========

You need to use the binary numbers in the diagnostic report to generate
two new binary numbers (called the gamma rate and the epsilon rate).
The power consumption can then be found by multiplying the gamma rate
by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common
bit in the corresponding position of all numbers in the diagnostic
report.

The epsilon rate is calculated by the least common bit from each
position is used.

Multiplying the gamma rate by the epsilon rate produces the power
consumption.
"""
from collections import Counter
