from .models import GameCategory
from .serializers import GameCategorySerializer


class GameCategoryMixin:
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer