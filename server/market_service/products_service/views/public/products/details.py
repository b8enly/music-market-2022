from rest_framework.pagination import DjangoPaginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from products_service.exceptions.service import ValidationException
from products_service.serializers.requests.products import (
    CategoryTypeProductsRequestSerializer,
    BrandTypeProductsRequestSerializer,
    CategoryProductsRequestSerializer,
    BrandProductsRequestSerializer,
    ProductDetailRequest
)
from products_service.serializers.responses.products import (
    CategoryTypeProductsResponseSerializer,
    BrandTypeProductsResponseSerializer,
    CategoryProductsResponseSerializer,
    BrandProductsResponseSerializer,
    ProductDetailResponseSerializer
)
from products_service.mappers.models import (
    CategoryMapper,
    ProductMapper,
    BrandMapper,
    TypeMapper
)

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

    request_serializer = CategoryProductsRequestSerializer().validate(attrs={
        "category_id": category_id,
        "page": page,
        "page_size": page_size
    })

    category = CategoryMapper.get_by_id(id=category_id)
    products = ProductMapper.find_by_category(
        category_id=request_serializer.category_id
    )

    paginator = DjangoPaginator(
        object_list=products,
        per_page=request_serializer.page_size
    )
    if paginator.num_pages < request_serializer.page:
        raise ValidationException(
            detail=f"page number too large, max - {paginator.num_pages}"
        )

    response_serializer = CategoryProductsResponseSerializer(
        paginator=paginator,
        page_number=request_serializer.page,
        category=category
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

    request_serializer = BrandProductsRequestSerializer().validate(attrs={
        "brand_id": brand_id,
        "page": page,
        "page_size": page_size
    })

    brand = BrandMapper.get_by_id(id=brand_id)
    products = ProductMapper.find_by_brand(brand_id=brand_id)

    paginator = DjangoPaginator(
        object_list=products,
        per_page=request_serializer.page_size
    )
    if paginator.num_pages < request_serializer.page:
        raise ValidationException(
            detail=f"page number too large, max - {paginator.num_pages}"
        )

    response_serializer = BrandProductsResponseSerializer(
        paginator=paginator,
        page_number=request_serializer.page,
        brand=brand
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

    request_serializer = CategoryTypeProductsRequestSerializer().validate(
        attrs={
            "category_id": category_id,
            "type_id": type_id,
            "page": page,
            "page_size": page_size
        }
    )

    category = CategoryMapper.get_by_id(id=category_id)
    type = TypeMapper.get_by_id(id=type_id)
    products = ProductMapper.find_by_category_and_type(
        category_id=category_id,
        type_id=type_id
    )

    paginator = DjangoPaginator(
        object_list=products,
        per_page=request_serializer.page_size
    )
    if paginator.num_pages < request_serializer.page:
        raise ValidationException(
            detail=f"page number too large, max - {paginator.num_pages}"
        )

    response_serializer = CategoryTypeProductsResponseSerializer(
        paginator=paginator,
        page_number=request_serializer.page,
        category=category,
        type=type
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

    request_serializer = BrandTypeProductsRequestSerializer().validate(attrs={
        "brand_id": brand_id,
        "type_id": type_id,
        "page": page,
        "page_size": page_size
    })

    brand = BrandMapper.get_by_id(id=brand_id)
    type = TypeMapper.get_by_id(id=type_id)
    products = ProductMapper.find_by_brand_and_type(
        brand_id=brand_id, 
        type_id=type_id
    )

    paginator = DjangoPaginator(
        object_list=products,
        per_page=request_serializer.page_size
    )
    if paginator.num_pages < request_serializer.page:
        raise ValidationException(
            detail=f"page number too large, max - {paginator.num_pages}"
        )

    response_serializer = BrandTypeProductsResponseSerializer(
        paginator=paginator,
        page_number=request_serializer.page,
        brand=brand,
        type=type
    )

    return Response(data=response_serializer.data)


@api_view(ALLOWED_METHODS)
def product_detail(request: Request, product_id: UUID) -> Response:
    ProductDetailRequest().validate(attrs={
        "product_id": product_id
    })

    product = ProductMapper.get_by_id(id=product_id)

    response_serializer = ProductDetailResponseSerializer(
        instance=[product],
        many=True
    )

    return Response(data=response_serializer.data[0])
