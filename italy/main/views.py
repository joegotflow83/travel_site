from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .models import Contact


class IndexView(TemplateView):


	template_name = 'main/index.html'


class AboutView(TemplateView):


	template_name = 'main/about.html'


class ContactCreate(CreateView):
   

    model = Contact
    fields = ['first_name', 'last_name', 'email']
    success_url = '/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)