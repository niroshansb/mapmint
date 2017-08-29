import sys
import os
import shutil
import libxml2
import osgeo.ogr
import libxslt
import zoo

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
