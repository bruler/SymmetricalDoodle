#!/usr/bin/env python 

from __future__ import print_function
import json
import os
import logging


##
## @brief      { reads configuration file }
##
## @return     { nothing }
##
def readConfig() :
	conf = read('config.json', 'r')
	