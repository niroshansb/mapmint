import sys
import os
import shutil
import libxml2
import osgeo.ogr
import libxslt
import zoo
import requests

def down(conf,inputs,outputs):
	try: 
		f = open(conf["main"]["dataPath"]+"/"+inputs["serviceN"]["value"]+inputs["name"]["value"]+".txt", 'w')
	except:
		return 4
	try:
		f.write(inputs["url"]["value"]+"\n");
	except:
		return 4
	outputs["Result"]["value"]=zoo._("Data Store ")+inputs["name"]["value"]+zoo._(" created")
	return zoo.SERVICE_SUCCEEDED

def save(conf,inputs,outputs):
	try:
		r = requests.get(inputs["url"]["value"]+"/wa/istsos/services?query=&page=1&start=0&limit=25")
	except:
		return 4	
	try: 
		f = open(conf["main"]["dataPath"]+"/"+"istsos"+"/"+inputs["name"]["value"]+".txt", 'w')
	except:
		return 4
	try:
		f.write(r.content);
	except:
		return 4
	outputs["Result"]["value"]=zoo._("Data Store ")+inputs["name"]["value"]+zoo._(" created")
	return zoo.SERVICE_SUCCEEDED
