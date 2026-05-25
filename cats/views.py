from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

from .models import Achievement, Cat
from .serializers import AchievementSerializer, CatSerializer
from .permissions import OwnerOrReadOnly  # ← добавить импорт


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    pagination_class = PageNumberPagination
    permission_classes = [OwnerOrReadOnly]  # ← добавить пермишен

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('color', 'birth_year', 'tags__slug')
    search_fields = ('name',)
    ordering_fields = ('name', 'birth_year')
    ordering = ('birth_year',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['get'], url_path='similar')
    def similar_cats(self, request, pk=None):
        """Возвращает похожих котов по общим тегам"""
        cat = self.get_object()
        tags = cat.tags.all()
        similar = Cat.objects.filter(tags__in=tags).exclude(id=cat.id).annotate(
            same_tags=Count('tags')
        ).order_by('-same_tags')[:10]
        serializer = self.get_serializer(similar, many=True)
        return Response(serializer.data)


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = None