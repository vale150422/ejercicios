from rest_framework import serializers
from api.models.post import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
