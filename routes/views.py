from django.views.generic import TemplateView

class MapView(TemplateView):
    template_name = 'map.html'
    
    
class VuetifyView(TemplateView):
    template_name = 'vuetify.html'
    
    
class DirectionsView(TemplateView):
    template_name = 'directions.html'
