from django.views.generic import TemplateView       
from django.shortcuts import HttpResponse, render

# Create your views here.
class HomePageView(TemplateView): # class BASED VIEW
    template_name = "pagesTemplates/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Luis"
        print(context)
        return context

    

# Solution Assignment 1
class AboutPageView(TemplateView):
    template_name = "pagesTemplates/about.html"

# Function based views
def contact_page(request):
    # print(request.__dict__)
    # return HttpResponse("Hello World from a FBV")

    contact_info = {
        "name" : "Luis",
        "address" : "Something 444, CA",
        "email": "austin.haist@sdgku.edu"
    }

    return render(request, "pagesTemplates/contact.html", contact_info)