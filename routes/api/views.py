from routes.models import Route, Coord
from routes.api.serializers import RouteSerializer, RouteDetailSerializer, CoordSerializer
from rest_framework import viewsets


class RouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Route.objects.all().order_by('name')
    serializer_class = RouteSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RouteDetailSerializer
        return super(RouteViewSet, self).get_serializer_class()


class CoordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer