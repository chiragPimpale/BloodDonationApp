from ast import Return
from rest_framework import views, permissions
from django.http import JsonResponse
from api.models import RequestToBloodBankModel
from api.serializers import *
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import Http404
from django.db.models import Q
from rest_framework import status
from django.contrib.auth.hashers import make_password

"""
get_user_model is the instance of custom created user model
"""
User = get_user_model()


"""
SignupAccount is a view class to accept json data from serializer and create new account
"""
class SignupAccount(views.APIView):
    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Account has been registered successfully"}, status=201)
        return JsonResponse(serializer.errors, status=200)



"""
Genratebank account
"""
class GenrateBank(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        User.objects.create(
            password = make_password("password"),
            email = "bloodbank@django.project",
            user_type = "bloodbank",
            is_active = True
        )
        return JsonResponse({"message": "Blood bank account has been created successfully"}, status=201)


"""
api view for getting response as JSON of all donors
"""
class GetAllDoner(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, donor, format=None):
        if donor == 'donor':
            doners = User.objects.filter(user_type=donor)
            serializer = DonerSerializer(doners, many=True)
        else:
            doners = User.objects.filter(blood_group=donor)
            serializer = DonerSerializer(doners, many=True)
        return Response(serializer.data, status=200)



""""
BooldDonationRequest is apiview to take json serialized data from json and create donation request
"""
class BooldDonationRequest(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = BllodRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message":"Blood request has been sent to the doner"}, status=201)
        return JsonResponse(serializer.errors, status=400)



""""
RequestToBloodBank is a api view to take serialized json data and create request
"""
class RequestToBloodBank(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = BloodBankRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message":"Secret key is generated, go to blood bank with the code!"}, status=201)
        return JsonResponse(serializer.errors, status=400)




"""
VerifyAcceptorSecret is apiview to take data from bllodbank and send as serialized json and verify token
"""
class VerifyAcceptorSecret(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = VerifySecretTokeSerializer(data=request.data)
        if serializer.is_valid():
            if RequestToBloodBankModel.objects.filter(secret_key=serializer.data["secret_key"]).exists():
                snippets = RequestToBloodBankModel.objects.get(secret_key=serializer.data["secret_key"])
                serializer = VerifySecretTokeSerializer(snippets)
                return Response(serializer.data)
        return JsonResponse(serializer.errors, status=200)



"""
LoginView is api view to take credentials as json and login
"""
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


"""
GetAuthenticatedUser is api view to retrive authenticated user as serialized json data
"""
class GetAuthenticatedUser(views.APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

"""
GellSecretTokenByUser is api view to retrive all secret key as json serialized for the accepter account
"""
class GellSecretTokenByUser(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return RequestToBloodBankModel.objects.filter(requested_by=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        token = self.get_object(id)
        serializer = AllTokenSerializer(token, many=True)
        return Response(serializer.data)


"""
GetAccepterAndDonor is api view to retrive all accepter and donor in the admin field
"""
class GetAccepterAndDonor(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        user = User.objects.filter(Q(user_type__icontains='accepter') | Q(user_type__icontains='donor') | Q(user_type__icontains='bloodbank'))
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

"""
RemoveUser is api view to remove user from database  
"""
class RemoveUser(views.APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    def delete(self, request, id, format=None):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""""
MyBloodRequests is api view to retrive all bllod acceter request as JSON
"""
class MyBloodRequests(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return BloodRequest.objects.filter(blood_requested_to=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        user = user = self.get_object(id)
        serializer = BllodRequestCheckSerializer(user, many=True)
        return Response(serializer.data)


"""
RemoveRequest is api view to remove request for blood donor
"""
class RemoveRequest(views.APIView):
    def get_object(self, pk):
        try:
            return BloodRequest.objects.get(pk=pk)
        except BloodRequest.DoesNotExist:
            raise Http404
    def delete(self, request, id, format=None):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)