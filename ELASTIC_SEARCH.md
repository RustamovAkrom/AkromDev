Для интеграции Elasticsearch с Django можно использовать библиотеку `django-elasticsearch-dsl`. Вот пошаговое руководство по настройке и использованию Elasticsearch в вашем Django-проекте.

### Установка необходимых библиотек
```bash
pip install django-elasticsearch-dsl
pip install elasticsearch
```

### Настройка `settings.py`
Добавьте настройки для Elasticsearch в ваш файл `settings.py`:
```python
# settings.py
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'  # или URL вашего Elasticsearch сервера
    },
}
```

### Создание документа для индексации
Создайте файл `documents.py` в вашем приложении и определите документы для индексации моделей.

```python
# documents.py
from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry
from .models import MyModel

# Определите индекс
my_model_index = Index('mymodels')

# Настройте индекс
my_model_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@registry.register_document
@my_model_index.doc_type
class MyModelDocument(Document):
    class Django:
        model = MyModel  # Модель, которую необходимо индексировать
        fields = [
            'name',
            'description',
            'created_at',
        ]
```

### Обновление модели
Если ваша модель еще не создана, создайте ее. В данном примере используется простая модель с полями `name`, `description` и `created_at`.

```python
# models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

### Настройка сигналов для автоматической индексации
Для автоматического обновления индексов при изменении данных в модели, настройте сигналы.

```python
# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import MyModel
from .documents import MyModelDocument

@receiver(post_save, sender=MyModel)
def update_document(sender, instance, **kwargs):
    MyModelDocument().update(instance)

@receiver(post_delete, sender=MyModel)
def delete_document(sender, instance, **kwargs):
    MyModelDocument().delete(instance)
```

### Регистрация сигналов
Зарегистрируйте сигналы в вашем приложении.

```python
# apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals
```

### Индексация данных
Для начальной индексации данных выполните команду:
```bash
python manage.py search_index --rebuild
```

### Поиск данных
Теперь вы можете выполнять поиск по индексированным данным с использованием документов.

```python
# views.py
from django.shortcuts import render
from .documents import MyModelDocument

def search(request):
    q = request.GET.get('q')
    if q:
        results = MyModelDocument.search().query("match", name=q)
    else:
        results = MyModelDocument.search()
    return render(request, 'search.html', {'results': results})
```

### Настройка шаблона для отображения результатов поиска
Создайте шаблон `search.html` для отображения результатов поиска.

```html
<!-- templates/search.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Search Results</title>
</head>
<body>
    <h1>Search Results</h1>
    <form method="GET">
        <input type="text" name="q" placeholder="Search..." value="{{ request.GET.q }}">
        <button type="submit">Search</button>
    </form>
    <ul>
        {% for result in results %}
            <li>{{ result.name }} - {{ result.description }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

Теперь ваше Django-приложение интегрировано с Elasticsearch, и вы можете выполнять полнотекстовый поиск по индексированным данным.