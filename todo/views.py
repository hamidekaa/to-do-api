from rest_framework.viewsets import ModelViewSet
from .serializers import Todo, TodoSerializers

class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


