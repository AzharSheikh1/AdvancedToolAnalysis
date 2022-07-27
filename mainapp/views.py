from .permissions import IsAdminOrReadOnly
from .filters import HexDataFilter
from .models import HexData, Hypothesis, Profile
from .serializers import HexDataSerializer, HypothesisCreateSerializer, HypothesisSerializer, ProfileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from django_filters.rest_framework import DjangoFilterBackend


class HexDataViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HexDataSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = HexDataFilter
    queryset = HexData.objects.all()
    search_fields = ['$source']
    ordering_fields = ['created_date']
    permission_classes = [IsAuthenticated]


class HypothesisViewSet(viewsets.ModelViewSet):
    queryset = Hypothesis.objects.select_related('user').all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT']:
            return HypothesisCreateSerializer
        return HypothesisSerializer


class ProfileViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (profile, created) = Profile.objects.get_or_create(
            user_id=self.request.user.id)
        if request.method == 'GET':
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProfileSerializer(profile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
