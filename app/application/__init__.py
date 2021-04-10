
import os
files = []
routes =[]
for root,dirs,files in os.walk(os.path.dirname(os.path.abspath(__file__))):
	files.extend(files)
	break
for route in files:
	routes.append(route[:-3])
__all__ = routes

from . import *

	