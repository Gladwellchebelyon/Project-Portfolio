from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    insights = models.TextField(null=True, blank=True)
    demo_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name

class TechIcon(models.Model):
    CATEGORY_CHOICES = [
        ('LANG', 'Programming Languages'),
        ('FRAME', 'Frameworks & Libraries'),
        ('TOOL', 'Development Tools'),
        ('CLOUD', 'Cloud & Platforms'),
        ('DB', 'Databases'),
        ('MOBILE', 'Mobile Development'),
        ('WEB', 'Web Services & APIs'),
        ('AI', 'AI & Data Science'),
        ('SEC', 'Security & Testing'),
        ('OTHER', 'Other Tech'),
    ]
    
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50, help_text="FontAwesome class (e.g., 'fab fa-python')")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='OTHER')
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
    
    class Meta:
        ordering = ['category', 'name']
        verbose_name = "Tech Icon"
        verbose_name_plural = "Tech Icons"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ForeignKey(
        TechIcon,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='skills',
        help_text='Select an icon for this skill'
    )
    proficiency = models.IntegerField(
        default=0,
        help_text='Proficiency level (0-100)',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-proficiency']
