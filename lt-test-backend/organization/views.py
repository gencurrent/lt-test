from django.shortcuts import render
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Branch, Employee
from .serializers import BranchSerializer, EmployeeSerializer


def euclidian_distance(pointA, pointB):
    return (
        ((pointA[0] - pointB[0]) ** 2) +
        ((pointA[1] - pointB[1]) ** 2)
    ) ** 0.5

class BranchListAPIView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    filterset_fields = ['name', 'id']
    ordering_fields = ['id', 'name']


    def get(self, request, *args, **kwargs):
        query = dict(request.GET)

        lon, lat = query.get('lon'), query.get('lat')
        if (lon is not None and lat is not None):
            # If latitude or longitude are in the query parameters

            # Get only 1st 'lat', 'lon' parameters, all the others are ignored
            lat, lon = float(lon[0]), float(lat[0])
            selected_point = (lon, lat)

            # Maximum possible distance
            min_distance = euclidian_distance((0, -180), (0, 180))

            min_found = min_distance
            qs_branches = self.queryset.all()
            if not qs_branches.count():
                return Response([])

            closest_branch = qs_branches[0]

            for branch in qs_branches:
                branch_point = (float(branch.latitude), float(branch.longitude))
                new_distance = euclidian_distance(branch_point, selected_point)
                if new_distance < min_found:
                    min_found = new_distance
                    closest_branch = branch
            print(closest_branch)
            return Response(dict(**BranchSerializer(closest_branch).data, distance=min_found))
        
        return super().get(request, *args, **kwargs)    


class EmployeeListAPIView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    queryset = Employee.objects.select_related('branch').all()
    serializer_class = EmployeeSerializer    
    filterset_fields = ['id', 'first_name', 'third_name', 'branch__name',]
    ordering_fields = ['id', 'first_name']

    