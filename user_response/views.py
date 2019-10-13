#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.models import User
# from django.http import Http404

# def index(request):
#     help_list=User.objects
#     context= {'help_list':'help_list'}
#     return render(request, 'user_response/help_list.html',context)
# from django.contrib.auth.models import User
from django.http import Http404
from user_response.serializers import UserSerializer,SaverSerializer
from .models import User,Saver
from django.http import HttpResponse
# from user_response.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.contrib import messages




class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get_save(self,pk):
        try:
            return Saver.objects.get(pk=pk)
        except Saver.DoesNotExist:
            raise Http404

    # def get(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     user = UserSerializer(user)
    #     return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        # User.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # @action(detail=False, methods=['get'])
    def get(self,request,pk,format=None):
        saver = self.get_save(pk)
        lat_saver = saver.lat
        lng_saver = saver.lng
        user_list = User.objects.all()
        maxa = 0
        pk_new = 0
        for user in user_list:
            if user.pickup==0:
                lat=user.lat
                lng=user.lng
                no = user.no_of_person
                severe = user.no_of_severe_person
                normal = no - severe
                cons = float(107642.62648)
                dist = (cons)*(abs(float(lat)-float(lat_saver))+abs(float(lng)-float(lng_saver)))
                calc = (1000/(600+dist))*(normal+2*severe)
                if calc > maxa:
                    maxa=calc
                    pk_new = user.req_no
        # if pk_new == 0:
            # return Response()
        user_g = self.get_object(pk_new)
        user_g.chng_pickup(1)
        saver.destination(pk_new)
        saver.chngfree(0)
        user_g = UserSerializer(user_g)
        return Response(user_g.data)


class SaverList(APIView):
    def get(self, request, format=None):
        users = Saver.objects.all()
        serializer = SaverSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SaverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SaverDetail(APIView):
    def get_object(self, pk):
        try:
            return Saver.objects.get(pk=pk)
        except Saver.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = SaverSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = SaverSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        # User.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def getuser(pk,format=None):
    #     saver = self.get_object(pk)
    #     lat_saver = self.lat
    #     lng_saver = self.lng
    #     user_list = User.objects.all()
    #     maxa = 0
    #     pk_new = 0
    #     for user in user_list:
    #         if user.pickup==0:
    #             lat=user.lat
    #             lng=user.lng
    #             no = user.no_of_person
    #             severe = user.no_of_severe_person
    #             normal = no - severe
    #             dist = abs(lat-lat_saver)+abs(lng-lng_saver)
    #             calc = (1000/(600+dist))*(normal+2*severe)
    #             if calc > max:
    #                 max=calc
    #                 pk_new = user.req_no
    #
    #     user_g = User.get_object(pk_new)
    #     user_g = UserSerializer(user_g)
    #     return Response(user_g.data)

# def get_object(pk):
#     try:
#         return User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         raise Http404
# def changestatus(request):
#     # user = self.get_object(pk)
#     # return HttpResponse("status changed")
#     pk=request.GET.get('pk')
#     user=get_object(pk)
#     # win32win32api.MessageBox(user)
#     # messages.info(request,'hi')
#     # console.log(user)
#     # if user:
#     user.chng_pickup(0)
#         # return HttpResponse("status changed")
#     return HttpResponse("status changed")

# class UpdateSaver(generics.UpdateAPIView):
#     queryset = Saver.objects.all()
#     serializer_class = SaverSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.name = request.data.get("name")
#         instance.save()
#
#         serializer = self.get_serializer(instance)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#
#         return Response(serializer.data)
