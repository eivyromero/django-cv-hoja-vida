#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

### Paso 2: Verificar que requirements.txt tenga gunicorn

Abre `requirements.txt` y verifica que contenga estas líneas (si no están, agrégalas):
```
gunicorn
whitenoise
dj-database-url