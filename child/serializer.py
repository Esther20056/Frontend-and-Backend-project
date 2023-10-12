from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
# from .models import login
from .models import User



class  peopleSerializer(serializers.ModelSerializer):
   class Meta :
      model = User
      # fields = ['first_name', 'last_name', 'email']
      fields = '__all__'

   def validate(self, data):

      # print(data)
      # if data['first_name'] == "lolade":
      if data['first_name'] == "" or data['last_name'] == "":
       
      #  raise ValueError("error")
       raise ValueError("input fields are required")
      
      else:
         return data
      
   def create(self, data):
      pw = data['password']

      # print(pw)
      encrypted_pwd = make_password(pw, "wedrfghgfcdxsawsedrtyuuj")

      user = User.objects.create(
         first_name = data['first_name'],
         last_name = data['last_name'],
         email = data['email'], 
         photo = data['photo'],
         phone = data['phone'],
         username = data['username'],
         password = encrypted_pwd
      )

      #       user.password = encrypted_pwd

      # print(encrypted_pwd)

      # return(data)
      return user

# class logSerializer(serializers.ModelSerializer):
#    class Meta :
#       model = login
#       fields ='__all__'
 
#    def validate (data):
#      print(data)
#      return(data)

class loginSerializer(serializers.Serializer):
   email = serializers.EmailField()
   password = serializers.CharField() 
   
   
   def loginuser(self, data):
      user = User.objects.filter(email = data['email']).first()

      if user is not None:
         original_pwd = data['password']
         encrypted_pwd = getattr(user,'password')

         check = check_password(original_pwd, encrypted_pwd)
      
         if check == True:
          
           user ={
              "firs_tname": getattr(user, "first_name"),
              "last_tname": getattr(user, "last_name"),
              "email": getattr(user, "email"),
              "id": getattr(user, "id"),
           }
           return user
      
         else:
           raise ValueError ("Invalid credentials")

      else:
         raise ValueError("Invalid credentials provided")