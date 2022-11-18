from products_service.models import Brand
from uuid import UUID


class BrandMapper:
    @staticmethod
    def get_brand_by_id(id: UUID) -> Brand:
        return Brand.objects.get(id=id)
