from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from courses import serializers, paginators
from courses.models import Category, Course
from rest_framework.response import Response


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = serializers.CategorySerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.CoursePaginator

    def get_queryset(self):
        queryset = self.queryset


        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            queryset = queryset.filter(category_id=cate_id)

        return queryset

    @action(methods=['get'], url_path='lesson', detail=True)
    def ger_lesson(self, request, pk):
        lesson = self.get_object().lesson_set.filter(active=True)

        q = self.request.query_params.get('q')
        if q:
            lesson = lesson.filter(subject__icontains=q)
        return Response(serializers.LessonSerializer(lesson, many=True).data, status=status.HTTP_200_OK)
