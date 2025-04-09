from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import TaskModel
from tasks.serializers import TaskSerializer

class TaskList(APIView):
    def get(self, request):
        tasks = TaskModel.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
