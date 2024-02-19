from rest_framework import serializers
from App1.models import AutorDb, FraseDb

#Serializador
class AutorDbSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = AutorDb
        fields = '__all__'
        
class AutorConFraseSerliazer(serializers.ModelSerializer):
    frases = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='frases-detail')
    class Meta:
        model = AutorDb
        fields = '__all__'
        
class FraseDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = FraseDb
        fields = '__all__'