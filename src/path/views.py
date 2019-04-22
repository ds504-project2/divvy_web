from django.shortcuts import render

from .algorithm.pipline import optimize

# Create your views here.

def path_calculate(request):
	path_img 	= None
	path 		= None
	dist_ls 	= None
	time_ls 	= None
	if(request.method == "POST"):
		start, end = request.POST.get("start"), request.POST.get("dest")
		# print(start, end)
		# print(type(start))
		path, dist_ls, time_ls = optimize(int(start), int(end))
		# print(dist_ls)
		# print(time_ls)
		dist_ls = [round(d, 2) for d in dist_ls]
		time_ls = [round(t/60, 2) for t in time_ls]
	context = {
		"path": path,
		"distance": dist_ls,
		"time": time_ls,
	}
	return render(request, "page.html", context)
