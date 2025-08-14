# Django REST Framework CRUD API

A simple Django REST Framework API for managing products with full CRUD operations.

## Features

- Complete CRUD operations for products
- Filtering by product name (partial match)
- Price range filtering
- Pagination
- Swagger/OpenAPI documentation
- Comprehensive test suite
- Proper HTTP status codes and error handling

## Product Model

Each product has the following fields:
- `id` - Auto-generated primary key
- `name` - Product name (required)
- `description` - Product description (optional)
- `price` - Product price (decimal, required)
- `created_at` - Timestamp when created
- `updated_at` - Timestamp when last updated

## API Endpoints

- `GET /api/products/` - List all products
- `GET /api/products/{id}/` - Retrieve a specific product
- `POST /api/products/` - Create a new product
- `PUT /api/products/{id}/` - Update an existing product
- `DELETE /api/products/{id}/` - Delete a product

### Query Parameters

- `name` - Filter products by partial name match
- `min_price` - Filter products with price greater than or equal to this value
- `max_price` - Filter products with price less than or equal to this value
- `page` - Page number for pagination

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd crud_drf
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. (Optional) Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/products/`

## Documentation

- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- ReDoc: `http://127.0.0.1:8000/api/redoc/`
- OpenAPI Schema: `http://127.0.0.1:8000/api/schema/`

## Example API Requests

### List all products
```bash
curl -X GET "http://127.0.0.1:8000/api/products/"
```

### Get a specific product
```bash
curl -X GET "http://127.0.0.1:8000/api/products/1/"
```

### Create a new product
```bash
curl -X POST "http://127.0.0.1:8000/api/products/" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Laptop",
       "description": "High-performance laptop",
       "price": "999.99"
     }'
```

### Update a product
```bash
curl -X PUT "http://127.0.0.1:8000/api/products/1/" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Updated Laptop",
       "description": "Updated high-performance laptop",
       "price": "1099.99"
     }'
```

### Delete a product
```bash
curl -X DELETE "http://127.0.0.1:8000/api/products/1/"
```

### Filter products by name
```bash
curl -X GET "http://127.0.0.1:8000/api/products/?name=laptop"
```

### Filter products by price range
```bash
curl -X GET "http://127.0.0.1:8000/api/products/?min_price=100&max_price=500"
```

### Pagination
```bash
curl -X GET "http://127.0.0.1:8000/api/products/?page=2"
```

## Running Tests

Run the test suite:
```bash
python manage.py test
```

Run tests with coverage (requires coverage.py):
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

## HTTP Status Codes

- `200 OK` - Successful GET, PUT requests
- `201 Created` - Successful POST requests
- `204 No Content` - Successful DELETE requests
- `400 Bad Request` - Invalid request data
- `404 Not Found` - Product not found

## Project Structure

```
crud_drf/
├── crud_drf/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── manage.py
├── requirements.txt
└── README.md
```

## Technologies Used

- Django 4.2.7
- Django REST Framework 3.14.0
- django-filter 23.3 (for filtering)
- drf-spectacular 0.26.5 (for OpenAPI documentation)
- SQLite (default database)