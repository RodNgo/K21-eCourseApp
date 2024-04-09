from rest_framework import viewsets, generics, parsers, status, permissions
from rest_framework.decorators import action
from courses import serializers, paginators
from courses.models import Category, Course, Lesson, User
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
        return Response(serializers.LessonDetailsSerializer(lesson, many=True).data, status=status.HTTP_200_OK)

class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.prefetch_related('tags').filter(active=True)
    serializers_class = serializers.LessonSerializer

    def get_permissions(self):
        if self.action in ['add_comment']:
            return [permissions.IsAuthenticated()]\
        return [permissions.AllowAny()]

    @action(methods=['get'], url_path='comments', detail=True)
    def get_comments(self, request, pk):
        comments = self.get_object().comment_set.select_related('user').order_by("-id")
        paginator = paginators.CommentPaginator()
        page = paginator.paginate_queryset(comments, request)
        if page is not None:
            serializer = serializers.CommentSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        return Response(serializers.CommentSerializer(comments, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'], url_path='comments', detail=True)
    def add_comments(self, request, pk):
        c = self.get_object().comment_set.create(content=request.data.get('content'),user=request.user)

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser, ]
