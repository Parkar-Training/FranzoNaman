from user.models import users_new
from rest_framework import serializers

class serializerClass(serializers.ModelSerializer):
   # acc_created = serializers.CharField(required=False)
    #userId = serializers.CharField(required=False)

    class Meta:
        model= users_new
        fields= '__all__'