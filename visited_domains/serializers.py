from rest_framework import serializers
class LinkSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70)