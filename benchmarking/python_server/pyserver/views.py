from django.http import HttpResponse
import utils
import time

def time_block(request):
	try:
		time_lapse = request.GET.get('seconds', 0.3)
		time.sleep(float(time_lapse))
		return HttpResponse("Slept for {sec} Seconds".format(sec = str(time_lapse)))
	except Exception as e:
		return HttpResponse("Job not completed due to Error:" + str(e))

def crud(request):
	try:
		utils.perform_crud()
		return HttpResponse("CRUD operations performed")
	except Exception as e:
		return HttpResponse("Job not completed due to Error:" + str(e))