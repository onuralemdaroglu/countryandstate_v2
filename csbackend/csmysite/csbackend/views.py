from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Countries, States
from .serializers import CountriesSerializer, StatesSerializer

# Create your views here.
class CountryStateList(APIView):
    def get(self, request, country_code):
        #country = Countries.objects.get(code=country_code)
        #states = States.objects.filter(countryId=country.pk)
        #states = States.objects.filter(countryId=country.id)
        states = States.objects.filter(countryId__code=country_code)
        serializer = StatesSerializer(states, many=True)
        return Response(serializer.data)
    

# Class based views
""" class CountryList(APIView):
    def get(self, request, format=None):
        countries = Countries.objects.all()
        serializer = CountriesSerializer(countries, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CountriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StateList(APIView):
    def get(self, request, format=None):
        states = States.objects.all()
        serializer = StatesSerializer(states, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """
        

    
""" @api_view(['GET', 'POST'])
def countries_list(request):
    if request.method == "GET":
        countries = Countries.objects.all()
        serializer = CountriesSerializer(countries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CountriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def state_list(request):
    if request.method == "GET":
        states = States.objects.all()
        serializer = StatesSerializer(states)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = StatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """



# Generic class-based views

class CountriesListCreate(generics.ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class StatesListCreate(generics.ListCreateAPIView):
    queryset = States.objects.all()
    serializer_class = StatesSerializer


class CountriesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class StatesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = States.objects.all()
    serializer_class = StatesSerializer





