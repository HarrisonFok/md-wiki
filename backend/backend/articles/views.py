from rest_framework.viewsets import ModelViewSet

from .models import Article
from .serializers import ArticleSerializer

class ArticlesViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer