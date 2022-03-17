from djoser.serializers import UserCreateSerializer
from app_user.models import SeekerProfile,RecruiterProfile
from .models import User

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','username','password','first_name','last_name','user_type')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        user = User.objects.create_user(**validated_data)
        if user_type==1:
            SeekerProfile.objects.create(user=user)
        elif user_type==2:
            RecruiterProfile.objects.create(user=user)        
        return user