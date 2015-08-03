from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#from django.utils import dateutil
from matplotlib import pylab
import matplotlib.pyplot
from pylab import *
#import Image
import PIL
import PIL.Image
from io import StringIO
from django.template import RequestContext, loader
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from .models import *

def graph(request):
	f = figure(1, figsize=(6,6))
	x = []
	y = []
	count = 0
	depressionscore = DepressionScore.objects.get(pk=1)
	for field in depressionscore._meta.get_fields():
		#return HttpResponse(getattr(depressionscore, field.name))
		y.append(getattr(depressionscore, field.name))
		x.append(count)
		count+=1
	del x[0]
	del y[0]
	#return HttpResponse(x)
	y.reverse()
	plot(x,y,linewidth=2)

	xlabel('week')
	ylabel('Depression Score')
	title('%s Depression Score improvement'% 'Arka')
	grid(True)

	#buffer = StringIO()
	#canvas = pylab.get_current_fig_manager().canvas
	#canvas.print_png(response)
	#graphIMG = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostring_rgb())
	#graphIMG.save(buffer, "PNG")
	#pylab.close()
	canvas = FigureCanvasAgg(f)
	response = HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response