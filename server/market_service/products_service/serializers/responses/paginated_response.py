from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.pagination import DjangoPaginator


class PaginatedResponse(Serializer):
    def __init__(
        self, 
        paginator: DjangoPaginator, 
        page_number: int,
        serializer: ModelSerializer
    ):
        super().__init__()
        self.paginator = paginator
        self.page = paginator.get_page(page_number)
        self.serializer = serializer

    def data(self):
        return {
            "count": self.paginator.count,
            "next": (
                None if not self.page.has_next() 
                else self.page.next_page_number()
            ),
            "previous": (
                None if not self.page.has_previous() 
                else self.page.previous_page_number()
            ),
            "page_size": self.paginator.per_page,
            "results": self.serializer(self.page.object_list, many=True).data
        }
