from rest_framework.pagination import DjangoPaginator
from rest_framework.serializers import Serializer


class PaginatedResponseSerializer(Serializer):
    def __init__(self, paginator: DjangoPaginator, page_number: int):
        self.paginator = paginator
        self.page = paginator.get_page(page_number)
        self._data = {
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
            "results": self.page.object_list
        }

    @property
    def data(self):
        return self._data
