from django.views.generic import TemplateView       


# Create your views here.
class HomePageView(TemplateView): # class BASED VIEW
    template_name = "pagesTemplates/home.html"

# Solution Assignment 1
class AboutPageView(TemplateView):
    template_name = "pagesTemplates/about.html"