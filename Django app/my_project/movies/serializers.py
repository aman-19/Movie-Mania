from rest_framework import serializers
from .models import Cast_List,Movies_list

class Movies_list_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Movies_list
        fields = ('id','movie_name' ,'rating' , 'year' )
