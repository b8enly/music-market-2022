# Generated by Django 4.1.1 on 2022-09-28 21:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import stocks_service.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('active_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('active_to', models.DateTimeField(default=stocks_service.models.next_day)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks_service.stocktype')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOnSale',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_id', models.UUIDField()),
                ('stock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks_service.stock')),
            ],
            options={
                'unique_together': {('id', 'stock_id', 'product_id')},
            },
        ),
    ]