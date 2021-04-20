from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self,request,format=None):
         an_apiview=[
          'uses http method as function (get,post,path,put,delete)',
          'is similar to a traditional  Django View',
          'Gives you the most control over your application config',
          'Is mapped manually to URLs'
         ]

         return Response({'message':'Hello','an_apiview':an_apiview})
