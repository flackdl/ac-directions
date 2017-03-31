from routes.models import Route, Directions
from routes.api.serializers import RouteSerializer, RouteDetailSerializer, DirectionsSerializer, DirectionsDetailSerializer
from rest_framework import viewsets


class RouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Route.objects.all().order_by('name')
    serializer_class = RouteSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RouteDetailSerializer
        return super(RouteViewSet, self).get_serializer_class()
        

class DirectionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Directions.objects.all()
    serializer_class = DirectionsSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DirectionsDetailSerializer
        return super(DirectionsViewSet, self).get_serializer_class()