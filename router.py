import os
import sys


router_path = f"./app/{sys.argv[-1]}"
fname = "/__init__.py"

try:
	os.mkdir(router_path)	
except Exception as e:
	print(e)

file = open(router_path+fname,"w")
file.write("""
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

	""")

file.close()