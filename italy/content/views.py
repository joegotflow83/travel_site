from django.shortcuts import render
from django.views.generic import View

from .models import City


class Top6(View):


	def get(self, request):
		"""Display the top 6 cities visited"""
		rome = City.objects.get(name='Rome')
		florence = City.objects.get(name='Florence')
		venice = City.objects.get(name='Venice')
		naples = City.objects.get(name='Naples')
		milan = City.objects.get(name='Milan')
		turin = City.objects.get(name='Turin')
		return render(request, 'content/city_list.html', {
				'rome': rome,
				'florence': florence,
				'venice': venice,
				'naples': naples,
				'milan': milan,
				'turin': turin
			})
