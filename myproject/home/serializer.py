from rest_framework import serializers
from .models import Todo,TodoTiming
import re

# Define a serializer for the Todo model
class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        # Use the Todo model
        model = Todo
        # Exclude 'created_at' and 'updated_at' fields from the serialization
        exclude = ["created_at", "updated_at"]
    
    # Custom validation method for the serializer
    def validate(self, data):
        
        # Validate the 'todo_title' field if it exists in the input data
        if data.get('todo_title'):
            
            todo_title = data['todo_title']
            # Regex to check for special characters
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
             # Ensure 'todo_title' does not contain special characters
            if not (regex.search(todo_title) == None):
                raise serializers.ValidationError(
                    "Title cannot contain special characters"
                )
                
            # Ensure 'todo_title' is longer than 3 characters
            if len(todo_title) <= 3:
                raise serializers.ValidationError("Todo-Title must be up to 3 characters")
               
        # Validate the 'todo_age' field if it exists in the input data
        if data.get('todo_age'):
            todo_age = data['todo_age']
            # Ensure 'todo_age' is 18 or above
            if not todo_age >= 18:
                raise serializers.ValidationError("Age must be 18 or above 18")
        
        # Ensure 'is_done' field is present in the input data
        if 'is_done' not in data:
            raise serializers.ValidationError({
                'is_done': "This field also required"
            })
        
        return data

class TimingTodoSerializer(serializers.ModelSerializer):
    # This will give only fields which we already sets and not include all the exclude field
    todo = TodoSerializer() 
    
    class Meta:
        model = TodoTiming
        exclude = ["created_at", "updated_at"]
        
        #this will give --> all the fields which we exclude
        # depth = 1