from products_service.models import Type
from uuid import UUID


class TypeMapper:
    @staticmethod
    def get_by_id(id: UUID) -> Type:
        return Type.objects.get(id=id)
