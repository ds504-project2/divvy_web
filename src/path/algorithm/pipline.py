import sys
import numpy as np
import os

from .global_optimal import Graph_global
from .divvy_optimal import Graph_Divvy

def load_data():
	root_path = os.getcwd()
	# time_path = os.path.join(root_path, "Preprocessing_by_Sam/time_matrix.csv")
	# dist_path = os.path.join(root_path, "Preprocessing_by_Sam/distance_matrix.csv")
	time_path = os.path.join(root_path, "path/algorithm/time_matrix.csv")
	dist_path = os.path.join(root_path, "path/algorithm/distance_matrix.csv")

	# load two matrices (time and distance)
	time_matrix = np.genfromtxt(time_path, delimiter=",")
	dist_matrix = np.genfromtxt(dist_path, delimiter=",")
	return time_matrix, dist_matrix


def optimize(starting, ending, time_span=1800):
	# load data
	time_matrix, dist_matrix = load_data()

	num_vert = dist_matrix.shape[0]
	# print("creating global graph of distance")
	# global_graph_dist = Graph_global(num_vert, dist_matrix, time_matrix)
	# print("creating global graph of time")
	# global_graph_time = Graph_global(num_vert, time_matrix, dist_matrix)
	print("creating divvy graph")
	divvy_graph = Graph_Divvy(num_vert, dist_matrix, time_matrix)
	
	# print("calculating global SP of distance")
	# g_path_dist, g_dist_dist, g_compare_time_dist = global_graph_dist.show_path_dist(starting, ending)
	# print("calculating global SP of time")
	# g_path_time, g_dist_time, g_compare_dist_time = global_graph_time.show_path_dist(starting, ending)
	print("calculating divvy SP")
	dv_path, dv_dist, dv_time = divvy_graph.Divvy_GJLS(starting, ending, time_span=time_span)
	# print("From %d to %d" % (starting, ending))
	# print("\nglobal based on distance")
	# print(g_path_dist, g_dist_dist, g_compare_time_dist)
	# print("\nglobal based on time")
	# print(g_path_time, g_dist_time, g_compare_dist_time)
	# print("\ndivvy path")
	# print(dv_path)
	# print("divvy distance")
	# print(dv_dist)
	# print("divvy time")
	# print(dv_time)
	return dv_path, dv_dist, dv_time


if __name__ == "__main__":
	tm, dm = load_data()
	# print(tm)
	# try from 0 to 5
	optimize(tm, dm, 0, 5)