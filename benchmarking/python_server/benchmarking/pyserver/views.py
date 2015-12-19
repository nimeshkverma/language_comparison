import time
from django.http import HttpResponse

def index(request):
	try:
		time_lapse = request.GET.get('seconds', 0.3)
		time.sleep(float(time_lapse))
		return HttpResponse("Slept for {sec} seconds".format(sec = str(time_lapse)))
	except Exception as e:
		return HttpResponse("Job not completed due to Error:" + str(e))
