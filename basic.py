#!/usr/bin/python
#
# basic.py
#
# Author: Zex

from person_pb2 import *
import socket as s
import random as rd
import string
import sys

basic = {
   'host' : 'localhost',
   'port' : 1170,
   'maxsize' : 512,
}
