from rest_framework import generics
from ..models import Food
from .serializers import SubjectSerializer 
from rest_framework.permissions import IsAdminUser
class SubjetListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = SubjectSerializer

class SubjectCreateView(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUser]

class SubjectUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUser]