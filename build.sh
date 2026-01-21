#!/bin/bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

3. Guarda el archivo

---

## **Paso 4: Crear archivo .gitignore**

1. En la raíz del proyecto, crea un archivo llamado **.gitignore**
2. Pega este contenido:
```
# Python
*.pyc
__pycache__/
*.py[cod]
*$py.class

# Django
*.log
db.sqlite3
db.sqlite3-journal
/staticfiles/
/media/

# Virtual Environment
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db