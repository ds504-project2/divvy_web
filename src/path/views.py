from django.shortcuts import render

from .algorithm.pipline import optimize
import geopandas as gpd
import pandas as pd
import requests
import json

# Create your views here.

def station_data():
	
	url = 'https://feeds.divvybikes.com/stations/stations.json'
	r  = requests.get(url)
	r_load = json.loads(r.text)
	print(r_load['executionTime'])
	df = pd.DataFrame.from_records(r_load['stationBeanList'])[['id','availableBikes','availableDocks','totalDocks','status','lastCommunicationTime','is_renting','longitude','latitude']]
	chart_data = df.to_dict(orient='records')
	chart_data = json.dumps(chart_data, indent=2)
	return(chart_data)

def geo_data():
	df3 = gpd.read_file('static/data/Chicago_BikePaths.geojson')
	df3 = df3.to_json()
	return df3

def map_idx_id():
	map_file = pd.read_csv("static/data/station_locations_2019_for_mapping.csv")
	id_ls = map_file["id"].tolist()
	return id_ls


def path_calculate(request):
	path_img 	= None
	path 		= None
	dist_ls 	= None
	time_ls 	= None
	chart_data = station_data()
	chart_data3 = geo_data()
	id_ls = map_idx_id()
	# print(id_ls)
	if(request.method == "POST"):
		start, end = request.POST.get("start"), request.POST.get("dest")
		# print(start, end)
		# print(type(start))
		start 	= id_ls.index(int(start))
		end 	= id_ls.index(int(end))
		path, dist_ls, time_ls = optimize(start, end)
		# print(dist_ls)
		# print(time_ls)
		path = [id_ls[p] for p in path]
		dist_ls = [round(d, 2) for d in dist_ls]
		time_ls = [round(t/60, 2) for t in time_ls]
	context = {
		"path": path,
		"distance": dist_ls,
		"time": time_ls,
		"chart_data": chart_data,
		"chart_data3": chart_data3
	}
	return render(request, "page.html", context)

