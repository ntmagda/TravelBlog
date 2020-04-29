from django.views import generic
from django.utils import timezone
from entry import models

class Index(generic.TemplateView):
    template_name = "effect_test/index_test.html"