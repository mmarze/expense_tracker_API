from restapi import models, serializers
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ExpenseListCreate(ListCreateAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
    filterset_fileds = ["category", "merchant"]
    permissions.classes = [IsAuthenticated]


class ExpenseRetrieveDelete(RetrieveDestroyAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
