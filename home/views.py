from rest_framework.decorators import api_view
from rest_framework.response import Response
# importing APIView decorator
from rest_framework.views import APIView


# importing models
from .models import Person, Course, Color

# importing serializer
from home.serializers import PeopleSerializer, CourseSerializer, ColorSerializer, LoginSerializer
# in order to save data or send it to the server, use POST API
# in order to get data or update the data, use GET API

@api_view(['GET', 'POST', 'PUT'])
def index(request):
    courses = {
        'course_name' : 'Python',
        'course_duration' : '2 months',
        'learn' : ['Numpy', 'Pandas', 'Django', 'Django Rest Framework']
    }
    if request.method =='POST':
       print("You hit a POST method")
       data = request.data 
       print("*****")
       print(data) #it will print the data sent by the Postman API

       final_data = {
           'course_data' : courses,
           'requested_data' : data
       }
       return Response(final_data)
    
    elif request.method == 'GET':
        print(request.GET.get('search'))
        print("You hit a GET method")
        return Response(courses)
    
    elif request.method == 'PUT':
        print("You hit a PUT method")
        data = request.data
        print("*****")
        print(data['age']) #this will show age data in the terminal from the Postman

        final_data = {
            'course_data' : courses,
            'requested_data' : data 
        }
        return Response(final_data)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        obj = Person.objects.all()
        serializer = PeopleSerializer(obj, many = True)  #if the length of the obj variable is more the 1 then we will use many=true
        return Response(serializer.data)
        
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'PUT':
        # first we will grab the data
        data = request.data
        # then we will convert the data into JSON
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    elif request.method == 'PATCH': #PATCH method supports partial update
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({"message" : " person deleted"})

@api_view(['POST', 'GET', 'PUT', 'PATCH', 'DELETE'])
def course(request):
    if request.method == 'POST':
        data = request.data
        serializer = CourseSerializer(data = data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'GET':
        objec = Course.objects.all()
        serializer = CourseSerializer(instance = objec, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        objec = Course.objects.get(id=data['id'])
        serializer = CourseSerializer(objec, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'PATCH':
        data = request.data
        objec = Course.objects.get(id=data['id'])
        serializer = CourseSerializer(objec, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    else:
        data = request.data
        objec = Course.objects.get(id=data['id'])
        serializer = CourseSerializer(objec, data=data)
        objec.delete()
        return Response({'message' : 'course deleted'})
    

@api_view(['POST', 'GET', 'PATCH', 'PUT', 'DELETE'])
def color(request):
    if request.method == 'POST':
        data = request.data
        serializer = ColorSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'GET':
        obj = Color.objects.all()
        serializer = ColorSerializer(instance=obj, many=True)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Color.objects.get(id=data['id'])
        serializer = ColorSerializer(data=data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        obj = Color.objects.get(id=data['id'])
        serializer = ColorSerializer(data=data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    else:
        data = request.data
        obj = Color.objects.get(id=data['id'])
        serializer = ColorSerializer(data=data, instance=obj)
        obj.delete()
        return Response({'message' : 'color deleted'})
   
@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
    if serializer.is_valid():
        data = serializer.validated_data
        print(data)
        return Response({'message' : 'success'})

    return Response(serializer.errors)

class PersonAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = ColorSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def get(self, request):
        return Response({"message" : "This is a GET request"})
    
    def put(self, request):
        return Response({"message" : "This is a PUT request"})
    
    def patch(self, request):
        return Response({"message" : "This is a patch request"})
    
    def delete(self, request):
        return Response({"message" : "This is a delete request"})