from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class SignUpUserView(APIView):
    permission_classes = [AllowAny]

    # request에 담긴 정보: username, first_name, last_name, email, password, phone, ...
    # user_id는 client가 보내주는 값이 아님. DB에 반영 시 자동으로 생성.
    # 즉, 현재 단계에서 user_id는 존재하지 않음!
    @staticmethod
    def post(request):
        # request에는 어떤 값이 담겨 있는가?
        print(f"request: {request}")
        print(f"request.data: {request.data})")

        # JSON -> Object
        user_serializer = UserSerializer(data=request.data)
        print(user_serializer)

        # user_serializer.is_valid(raise_exception=True) -> 굳이 에러 커스텀 안 할 거라면?

        if user_serializer.is_valid():
            # DB에 저장 -> user_id가 생성됨
            user_saved = user_serializer.save()  # DB에 저장된 유효한 상태. 수정하면 좋지 않음..
            print(f"user_saved: {user_saved}")

            # client 측에 돌려줄 응답 객체 생성
            # print(Response)
            return Response({"user": user_serializer.data}, status=status.HTTP_201_CREATED)
        print(user_serializer.errors)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        print(user)

        if user:
            # token = TokenObtainPairSerializer.get_token(user)
            token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxOTYxMjcyLCJpYXQiOjE2NjE4NzQ4NzIsImp0aSI6IjU3NjRlYTdhYmQwNTQ1ODZiYmIyOTM3OTg4Y2JkMGY1Iiwibmlja25hbWUiOjJ9.jtxVhDmSrHSHW1IhdeWGl6QHy4kVOPjpTMYfrmWbnQ0"
            refresh_token = str(token)
            access_token = str(token.access_token)

            res = Response(
                {
                    "refresh": str(token),
                    "access": str(token.access_token),
                },
                status=status.HTTP_200_OK,
            )
            return res
        return Response(status=status.HTTP_401_UNAUTHORIZED)


