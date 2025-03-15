from rest_framework import serializers

from .models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = [user_nickname] pode ser campo a campo, por exemplo