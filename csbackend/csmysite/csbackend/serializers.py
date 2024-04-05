from rest_framework import serializers
from .models import Countries, States

# Countries

class CountriesSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, read_only=True)
    code = serializers.CharField(required=False, max_length=2)
    name = serializers.CharField(required=False, max_length=60)

    def create(self, validated_data):
        """
        Create and return a new `Countries` instance, given the validated data.
        """
        return Countries.objects.create(**validated_data)

    
# States

class StatesSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, read_only=True)
    code = serializers.CharField(required=False, max_length=3)
    name = serializers.CharField(required=False, max_length=60)
    countryId_id = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `States` instance, given the validated data.
        """
        return States.objects.create(**validated_data)


# Using ModelSerializer
""" class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['id', 'code', 'name'] """
       

# Using ModelSerializer
""" class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ['id', 'code', 'name', 'countryId'] """
