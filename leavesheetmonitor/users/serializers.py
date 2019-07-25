from rest_framework import serializers
from leavesheetmonitor.users.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('psa_id', 'role', 'manager_psa_id', 'manager_name', 'manager_email')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Bifrost user writable nested serializer
    """
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.psa_id = profile_data.get('psa_id', profile.psa_id)
        profile.role = profile_data.get('role', profile.role)
        profile.manager_psa_id = profile_data.get('manger_psa_id', profile.manager_psa_id)
        profile.manager_name = profile_data.get('manager_name', profile.manager_name)
        profile.manager_email = profile_data.get('manager_email', profile.manager_email)
        profile.save()

        return instance
