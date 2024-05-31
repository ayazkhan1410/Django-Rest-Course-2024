from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TimingTodoSerializer, TodoSerializer  
from .models import Todo, TodoTiming
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action



class TodoViewSet(viewsets.ModelViewSet):
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    @action(detail=False, methods=['GET'], url_path='get-timing-todo')
    def get_timing_todo(self, request):
        try:
            timin_obj = TodoTiming.objects.all()  # Get all Todo items from the database
            serializer = TimingTodoSerializer(timin_obj, many=True)  # Serialize the data
                
            return Response({
                    'status': 200,
                    'message': 'Todos fetched successfully',
                    'data': serializer.data
            })
            
        except Exception as e:
            return Response({
                'status': False,
                'data': serializer.errors
            })
    
    @action(detail=False, methods=['post'], url_path='add-data-to-todo')
    def add_data_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
               
                return Response({
                    'status': 200,
                    'message': 'Success Data',
                    'data': serializer.data
                })
            else:
                return Response({
                    'status': 400,
                    'message': 'Something went wrong',
                    'data': serializer.errors
                })
                       
        except Exception as e:
            print(e)
            return Response({
                    'status': 400,
                    'message': 'something went wrong'
            })


# API view is used to convert django existing function into a API
@api_view(['GET', 'POST', 'PATCH'])
def index(request):
    if request.method == "GET":
        # Respond to a GET request
        return Response({
            'status': 200,
            "message": "You called GET request"
        })
    elif request.method == "POST":
        # Respond to a POST request
        return Response({
            'status': 200,
            "message": "You called POST request"
        })
    elif request.method == "PATCH":
        # Respond to a PATCH request
        return Response({
            'status': 200,
            "message": "You called PATCH request"
        })
    else:
        # Respond to any other request method (invalid)
        return Response({
            "status": 400,
            "message": "You called an invalid request"
        })

# Define an API view to handle creating a new Todo
@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data  # Get the data from the request
        serializer = TodoSerializer(data=data)  # Create a serializer instance with the data
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "Success, data saved",
                'data': serializer.data 
            })
        else:
            return Response({
                'status': False,
                'message': "Invalid data",
                'data': serializer.errors  # Return the validation errors
            })
    except Exception as e:
        print(e) 
        return Response({
            'status': False,
            'message': "Something went wrong"
        })

# Retrieve the data
@api_view(['GET'])
def get_todo(request):
    try:
        todos = Todo.objects.all()  # Get all Todo items from the database
        serializer = TodoSerializer(todos, many=True)  # Serialize the data
        
        return Response({
            'status': 200,
            'message': 'Todos fetched successfully',
            'data': serializer.data
        })
        
    except Exception as e:
        print(e) 
        return Response({
            'status': False,
            'message': "Something went wrong"
        })

# Create Data
@api_view(['POST'])
def todo_age(request):
    try:
        data = request.data  # Get the data from the request
        serializer = TodoSerializer(data=data)  # Create a serializer instance with data
        
        if serializer.is_valid():
            serializer.save()  
            return Response({
                'status': 200,
                'message': "Age fetched",
                'data': serializer.data  
            })
        else:
            return Response({
                'status': 400,
                'message': "Invalid data",
                'data': serializer.errors  
            })
    except Exception as e:
        print(e) 
        return Response({
            'status': 400,
            'message': "Something went wrong"
        })


# Partial Update the data
@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        uuid = data.get('uuid')
        
        if not uuid:
            return Response({
                'status': 400,
                'message' : {}
            })
        
        objs = Todo.objects.get(uuid = data.get('uuid'))
        serializer = TodoSerializer(objs, data = data, partial  = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'Data Update successfully',
                'data': serializer.data
            })
        else:
            return Response({
                'status': 400,
                'data': serializer.errors
            })
        
    
    except Exception as e:
        print(e)
        return Response({
            'status': 400,
            'message': "Something went wrong"
        })



# My own Practice starts from here  

# Creating Todo in DRF
@api_view(['POST'])
def create_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':200,
                'message': 'Your data has been fetched and created succesfully',
                'data':serializer.data
            })
            
        else:
            return Response({
                'status': 400,
                'message': "Data required",
                'data': serializer.errors
            })
            
    except Exception as e:
        print(e)
        return Response({
            'status': 400,
            'message': "Something went wrong"
        })

# Updating Data in DRF
@api_view(['PATCH'])
def update_todo(request):
    try:
        data = request.data
        uuid = data.get('uuid')
        if not uuid:
            return Response({
                'status': 400,
                'message': "UUID required or UUID must be matched with database UUID"
            })
        todo_obj = Todo.objects.get(uuid = data.get('uuid'))
        serializer = TodoSerializer(todo_obj, data=data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": 200,
                "message": "Database Updated Successfully",
                'data': serializer.data
            })
        else:
            return Response({
                'status': 400,
                'message': serializer.errors
            })
            
    except Exception as e:
        print(e)
        return Response({
            'status': 400,
            'message': 'something went wrong'
        })

# retrieves data
@ api_view(['GET'])
def retrieves_data(request):
    try:
        todo_objs = Todo.objects.all() # Taking all data from database
        serializer = TodoSerializer(todo_objs, many = True)
        
        return Response({
            'status': 200,
            'message': "retrieving The data",
            'data': serializer.data
        })
        
    except Exception as e:
        print(e)
        return Response({
                'status': 400,
                'data': serializer.errors
            })
        
# partially updating the data
@api_view(['PATCH'])
def partial_update(request):
    try:
        data = request.data
        uuid = data.get('uuid')
        if not uuid:
            return Response({
                'status': 400,
                'message': "Enter valid UUID"
            })
        
        todo_objs = Todo.objects.get(uuid = data.get('uuid'))
        serializer = TodoSerializer(todo_objs, data = data,  partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message':'data updated successfully',
                'data': serializer.data
            })
        else:
            return Response({
                'status': 400,
                'message': 'Cannot update the data',
                'data': serializer.errors
            })
    except Exception as e:
        print("Exception = ", e)
        return Response({
            'status': 400,
            'message':'Something went wrong'
        })
        
@api_view(['DELETE'])
def delete_data(request):
    try:
        data = request.data
        uuid = data.get('uuid')
        if not uuid:
            return Response({
                'status': 400,
                'message': "Enter valid UUID"
            })
        
        todo_objs = Todo.objects.get(uuid = data.get('uuid'))
        todo_objs.delete()
        return Response({
            'status': 200,
            'message': 'Todo deleted Successfully'
        })
        
    
    except Exception as e:
        print("Exception = ", e)
        return Response({
            'status': 400,
            'message':'Something went wrong'
        })


class TodoView(APIView):
    
    def post(self, request):
        try:
            data = request.data
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Todo created successfully',
                    'data': serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status': 400,
                    'message': 'Unable to create todo',
                    'data': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Something went wrong'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request):
        try:
            todo_objs = Todo.objects.all()
            serializer = TodoSerializer(todo_objs, many=True)
            return Response({
                'status': 200,
                'message': 'Retrieving the data',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Something went wrong'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def patch(self, request):
        try:
            data = request.data
            uuid = data.get('uuid')
            if not uuid:
                return Response({
                    'status': 400,
                    'message': "Enter valid UUID"
                })
            
            todo_objs = Todo.objects.get(uuid = data.get('uuid'))
            serializer = TodoSerializer(todo_objs, data = data,  partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message':'data updated successfully',
                    'data': serializer.data
                })
            else:
                return Response({
                    'status': 400,
                    'message': 'Cannot update the data',
                    'data': serializer.errors
                })
        except Exception as e:
            print("Exception = ", e)
            return Response({
                'status': 400,
                'message':'Something went wrong'
            })
            
    def delete(self, request):
        try:
            data = request.data
            uuid = data.get('uuid')
            if not uuid:
                return Response({
                    'status': 400,
                    'message': "Enter valid UUID"
                })
            
            todo_objs = Todo.objects.get(uuid = data.get('uuid'))
            todo_objs.delete()
            return Response({
                'status': 200,
                'message': 'Todo deleted Successfully'
            })
            
        
        except Exception as e:
            print("Exception = ", e)
            return Response({
                'status': 400,
                'message':'Something went wrong'
            })

