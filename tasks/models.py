from django.db import models
from django.contrib.auth.models import User


# ==================== PERFIL ====================
class Profile(models.Model):
    """Perfil profesional único"""
    name = models.CharField(max_length=200, default="Eivy René Romero Mendoza")
    title = models.CharField(max_length=200, default="Full Stack Developer")
    email = models.EmailField(default="eivyromero.26@gmail.com")
    phone = models.CharField(max_length=50, default="+593 98 721 3633")
    location = models.CharField(max_length=200, default="Guayaquil, Ecuador")
    description = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfil"


# ==================== HABILIDADES ====================
class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Base de Datos'),
        ('tools', 'Herramientas'),
        ('other', 'Otros'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    icon = models.CharField(max_length=10, default='💻')
    level = models.IntegerField(default=50, help_text="Nivel de 0 a 100")
    order = models.IntegerField(default=0, help_text="Orden de visualización")
    
    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


# ==================== EXPERIENCIA LABORAL ====================
class Experience(models.Model):
    company = models.CharField(max_length=200, verbose_name="Empresa")
    position = models.CharField(max_length=200, verbose_name="Cargo")
    description = models.TextField(verbose_name="Descripción")
    start_date = models.CharField(max_length=50, verbose_name="Fecha de inicio")
    end_date = models.CharField(max_length=50, blank=True, null=True, verbose_name="Fecha de fin")
    is_current = models.BooleanField(default=False, verbose_name="Trabajo actual")
    technologies = models.CharField(max_length=500, blank=True, verbose_name="Tecnologías usadas")
    order = models.IntegerField(default=0, help_text="Orden de visualización")
    
    class Meta:
        ordering = ['-order', '-start_date']
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
    
    def __str__(self):
        return f"{self.position} en {self.company}"


# ==================== EDUCACIÓN ====================
class Education(models.Model):
    institution = models.CharField(max_length=200, verbose_name="Institución")
    degree = models.CharField(max_length=200, verbose_name="Título/Grado")
    field_of_study = models.CharField(max_length=200, blank=True, null=True, verbose_name="Campo de estudio")
    start_date = models.CharField(max_length=50, verbose_name="Fecha de inicio")
    end_date = models.CharField(max_length=50, blank=True, null=True, verbose_name="Fecha de fin")
    description = models.TextField(blank=True, verbose_name="Descripción")
    is_current = models.BooleanField(default=False, verbose_name="En curso")
    order = models.IntegerField(default=0, help_text="Orden de visualización")

    class Meta:
        ordering = ['-order', '-start_date']
        verbose_name = "Educación"
        verbose_name_plural = "Educación"

    def __str__(self):
        return f"{self.degree} - {self.institution}"


# ==================== CURSOS Y CERTIFICACIONES ====================
class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del curso")
    institution = models.CharField(max_length=200, verbose_name="Institución/Plataforma")
    date = models.CharField(max_length=50, verbose_name="Fecha")
    duration = models.CharField(max_length=100, blank=True, verbose_name="Duración")
    description = models.TextField(blank=True, verbose_name="Descripción")
    certificate_url = models.URLField(blank=True, verbose_name="URL del certificado")
    order = models.IntegerField(default=0, help_text="Orden de visualización")
    
    class Meta:
        ordering = ['-order', '-date']
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
    
    def __str__(self):
        return f"{self.name} - {self.institution}"


# ==================== RECONOCIMIENTOS ====================
class Award(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    organization = models.CharField(max_length=200, verbose_name="Organización")
    date = models.CharField(max_length=50, verbose_name="Fecha")
    description = models.TextField(blank=True, verbose_name="Descripción")
    order = models.IntegerField(default=0, help_text="Orden de visualización")
    
    class Meta:
        ordering = ['-order', '-date']
        verbose_name = "Reconocimiento"
        verbose_name_plural = "Reconocimientos"
    
    def __str__(self):
        return f"{self.title} - {self.organization}"


# ==================== PROYECTOS ====================
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    technologies = models.CharField(max_length=200, blank=True, verbose_name="Tecnologías")
    url = models.URLField(blank=True, verbose_name="URL del proyecto")
    github_url = models.URLField(blank=True, verbose_name="URL de GitHub")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name="Imagen")
    start_date = models.CharField(max_length=50, blank=True, verbose_name="Fecha de inicio")
    end_date = models.CharField(max_length=50, blank=True, null=True, verbose_name="Fecha de fin")
    is_featured = models.BooleanField(default=False, verbose_name="Destacado")
    order = models.IntegerField(default=0, help_text="Orden de visualización")
    
    class Meta:
        ordering = ['-order', '-start_date']
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
    
    def __str__(self):
        return self.title


# ==================== SERVICIOS ====================
class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del servicio")
    description = models.TextField(verbose_name="Descripción")
    icon = models.CharField(max_length=10, default='🔧', verbose_name="Icono")
    price_info = models.CharField(max_length=200, blank=True, verbose_name="Información de precio")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    order = models.IntegerField(default=0, help_text="Orden de visualización")
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
    
    def __str__(self):
        return self.name


# ==================== TAREAS (YA EXISTENTE) ====================
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"