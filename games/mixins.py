from gamesapi_por_fazer.games.models import GameCategory
from gamesapi_por_fazer.games.serializers import GameCategorySerializer


class GameCategoryMixin:
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer