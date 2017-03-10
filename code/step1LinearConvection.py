#!/usr/bin/env python

# Solve the 1-D Linear convection equation:
# $\frac{\partial u}{\partial t} + c \frac{\partial u}{\partial x} = 0$
# Time derivative: Forward Difference scheme
# Space derivative: Backward Difference scheme

import numpy
from matplotlib import pyplot
import time,sys
