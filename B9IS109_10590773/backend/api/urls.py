from django.urls import path
from api.views import *


urlpatterns = [
    path("api/login/", LoginView.as_view(), name="LoginView"),
    path("api/signup/", SignupAccount.as_view(), name="SignupAccount"),
    path("api/all-doners/<str:donor>/", GetAllDoner.as_view(), name="GetAllDoner"),
    path("api/request-donation/", BooldDonationRequest.as_view(), name="BooldDonationRequest"),
    path("api/request-blood-bank/", RequestToBloodBank.as_view(), name="RequestToBloodBank"),
    path("api/verify-secret/", VerifyAcceptorSecret.as_view(), name="VerifyAcceptorSecret"),
    path("api/user/<int:id>/", GetAuthenticatedUser.as_view(), name="GetAuthenticatedUser"),
    path("api/all-tokens/<int:id>/", GellSecretTokenByUser.as_view(), name="GellSecretTokenByUser"),
    path("api/all-users/", GetAccepterAndDonor.as_view(), name="GetAccepterAndDonor"),
    path("api/user/<int:id>/remove/", RemoveUser.as_view(), name="RemoveUser"),
    path("api/my-request/<int:id>/", MyBloodRequests.as_view(), name="MyBloodRequests"),
    path("api/my-request/remove/<int:id>/", RemoveRequest.as_view(), name="RemoveRequest"),
    path("api/generate-bank-account/", GenrateBank.as_view(), name="GenrateBank"),
]