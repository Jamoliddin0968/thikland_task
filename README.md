# My Django and Elasticsearch Application

Bu loyiha Django REST Framework (DRF) yordamida Product CRUD API'sini yaratish, PostgreSQL ma'lumotlar bazasidan foydalanish, JWT autentifikatsiyasi orqali autentifikatsiya qilish va Elasticsearch bilan integratsiya qilish uchun mo'ljallangan. Loyiha Docker Compose yordamida ishga tushiriladi.

## Talablar

Loyihani ishga tushirishdan oldin quyidagi dasturlar o'rnatilgan bo'lishi kerak:

- Docker
- Docker Compose

## O'rnatish

Quyidagi qadamlarni bajarib, loyihani o'rnatish va ishga tushirish mumkin.
### 1.

```bash
    $git clone https://github.com/username/repository.git
    $cd repository


### 2.

```bash
   $docker-compose up -d


### 3.

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --noinput

### 4

```bash
docker-compose exec web python manage.py search_index --rebuild
