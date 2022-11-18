from rest_framework.pagination import DjangoPaginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from products_service.mappers.models.category_mapper import CategoryMapper
from products_service.mappers.models.product_mapper import ProductMapper
from products_service.mappers.models.brand_mapper import BrandMapper
from products_service.serializers.responses.paginated_response import (
    ProductsPaginatedResponse
)
from products_service.serializers.responses.products_response import (
    ProductSerializer
)
from products_service.serializers.responses.category_response import (
    CategorySerializer
)
from products_service.serializers.requests.products_requests import (
    CategoryProductsRequest
)
from products_service.serializers.requests.brands_requests import (
    BrandProductsRequest
)
from products_service.serializers.responses.brand_response import (
    BrandSerializer
)
from products_service.serializers.requests.products_requests import CategoryTypeProductsRequest
from products_service.serializers.requests.brands_requests import BrandTypeProductsRequest
from products_service.serializers.requests.products_requests import ProductDetailRequest
from products_service.serializers.responses.products_response import ProductSerializer

from uuid import UUID


ALLOWED_METHODS = ["GET"]


@api_view(ALLOWED_METHODS)
def category_products(request: Request, category_id: UUID) -> Response:
    query_page = request.query_params.get("page")
    json_page = request.data.get("page")
    page = json_page if query_page is None else query_page

    query_page_size = request.query_params.get("page_size")
    json_page_size = request.data.get("page_size")
    page_size = json_page_size if query_page_size is None else query_page_size

    request_serializer = CategoryProductsRequest().validate(attrs={
        "category_id": category_id,
        "page": page,
        "page_size": page_size
    })

    products = ProductMapper.find_products_by_category(
        category_id=request_serializer.category_id
    )

    paginator = DjangoPaginator(
        object_list=products,
        per_page=request_serializer.page_size
    )

    response_serializer = ProductsPaginatedResponse(
        paginator=paginator,
        page_number=request_serializer.page
    )

    return Response(data=response_serializer.data)


@api_view(ALLOWED_METHODS)
def brand_products(request: Request, brand_id: UUID) -> Response:
    query_page = request.query_params.get("page")
    json_page = request.data.get("page")
    page = json_page if query_page is None else query_page

    query_page_size = request.query_params.get("page_size")
    json_page_size = request.data.get("page_size")
    page_size = json_page_size if query_page_size is None else query_page_size

    request_serializer = BrandProductsRequest().validate(attrs={
        "brand_id": brand_id,
        "page": page,
        "page_size": page_size
    })

    products = ProductMapper.find_products_by_brand(brand_id=brand_id)

    paginator = DjangoPaginator(
        object_list=products,
        per_page=request_serializer.page_size
    )

    response_serializer = ProductsPaginatedResponse(
        paginator=paginator,
        page_number=request_serializer.page
    )

    return Response(data=response_serializer.data)


@api_view(ALLOWED_METHODS)
def category_type_products(
    request: Request, 
    category_id: UUID, 
    type_id: UUID
) -> Response:
    query_page = request.query_params.get("page")
    json_page = request.data.get("page")
    page = json_page if query_page is None else query_page

    query_page_size = request.query_params.get("page_size")
    json_page_size = request.data.get("page_size")
    page_size = json_page_size if query_page_size is None else query_page_size

    request_serializer = CategoryTypeProductsRequest().validate(attrs={
        "category_id": category_id,
        "type_id": type_id,
        "page": page,
        "page_size": page_size
    })

    products = ProductMapper.find_by_category_and_type(
        category_id=category_id,
        type_id=type_id
    )

    paginator = DjangoPaginator(
        object_list=products,
        per_page=request_serializer.page_size
    )

    response_serializer = ProductsPaginatedResponse(
        paginator=paginator,
        page_number=request_serializer.page
    )

    return Response(data=response_serializer.data)


@api_view(ALLOWED_METHODS)
def brand_type_products(
    request: Request,
    brand_id: UUID,
    type_id: UUID
) -> Response:
    query_page = request.query_params.get("page")
    json_page = request.data.get("page")
    page = json_page if query_page is None else query_page

    query_page_size = request.query_params.get("page_size")
    json_page_size = request.data.get("page_size")
    page_size = json_page_size if query_page_size is None else query_page_size

    request_serializer = BrandTypeProductsRequest().validate(attrs={
        "brand_id": brand_id,
        "type_id": type_id,
        "page": page,
        "page_size": page_size
    })

    products = ProductMapper.find_by_brand_and_type(
        brand_id=brand_id, 
        type_id=type_id
    )

    paginator = DjangoPaginator(
        object_list=products,
        per_page=request_serializer.page_size
    )

    response_serializer = ProductsPaginatedResponse(
        paginator=paginator,
        page_number=request_serializer.page
    )

    return Response(data=response_serializer.data)


@api_view(ALLOWED_METHODS)
def product_detail(request: Request, product_id: UUID) -> Response:
    ProductDetailRequest().validate(attrs={
        "product_id": product_id
    })

    product = ProductMapper.get_by_id(id=product_id)

    response_serializer = ProductSerializer(instance=[product], many=True)

    return Response(data=response_serializer.data)
