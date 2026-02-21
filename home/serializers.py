# serializers helps to convert the models into JSON and validates the incoming data

from rest_framework import serializers
from . models import Person, Course, Color


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
    
    #using serializers method field to add the custom resistence field
    water_resistence = serializers.SerializerMethodField()

    #using the prefix to show the method field will look like in the frontend
    def get_water_resistence(self, obj):
        return{'water_resistence' : 'high'}


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person 
        fields = '__all__' #we will serialize all the fields which are in models
    
    color = ColorSerializer(many = False)
    # using serializers method field to add custom field named color_info
    color_info = serializers.SerializerMethodField()

    #using prefix to show how the color_info field will look in the frontend
    def get_color_info(self, obj):
        color_obj = Color.objects.get(id = obj.color.id)

        return {'color_name' : color_obj.color_name, 'hex_code' : '#000'}
    
    #validating the age 
    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater then 18')
        return data
    
    #validating the gender
    def validate(self, data):
        if data['gender'] == 'Transgender':
            raise serializers.ValidationError('gender should be male/female or NA')
        return data
       
class CourseSerializer(serializers.ModelSerializer):

    #using serializer method to add the custom field course_duration
    course_duration = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = '__all__'

    #using the prefix get_course_duration to show how it is displayed in the frontend 
    def get_course_duration(self):
        return {
            'course_duration': '1 year', 
        }
    
    #validating the fees
    def validate_fees(self, value):
        if value < 100000:
            raise serializers.ValidationError(
                'fees should be greater than 100000'
            )
        return value
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

