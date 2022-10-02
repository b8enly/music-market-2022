from rest_framework.decorators import api_view
from rest_framework.response import Response
from ....serializers import UserModelSerializer


@api_view(["POST"])
def create_user(request):

    serializer = UserModelSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)