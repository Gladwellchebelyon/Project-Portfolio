from django.db import migrations

def create_initial_data(apps, schema_editor):
    TechIcon = apps.get_model('portfolio_app', 'TechIcon')
    Skill = apps.get_model('portfolio_app', 'Skill')
    Project = apps.get_model('portfolio_app', 'Project')
    
    # Create tech icons
    icons = {
        'fab fa-python': ('Python', 'LANG'),
        'fab fa-js': ('JavaScript', 'LANG'),
        'fab fa-html5': ('HTML5', 'LANG'),
        'fab fa-css3-alt': ('CSS3', 'LANG'),
        'fab fa-react': ('React', 'FRAME'),
        'fab fa-node-js': ('Node.js', 'FRAME'),
        'fab fa-django': ('Django', 'FRAME'),
        'fab fa-git-alt': ('Git', 'TOOL'),
        'fas fa-database': ('Database', 'DB'),
        'fas fa-brain': ('Machine Learning', 'AI'),
    }
    
    tech_icons = {}
    for class_name, (name, category) in icons.items():
        icon = TechIcon.objects.create(
            name=name,
            class_name=class_name,
            category=category
        )
        tech_icons[class_name] = icon
    
    # Create skills
    skills_data = [
        ('Python', 'fab fa-python', 90),
        ('JavaScript', 'fab fa-js', 85),
        ('HTML5', 'fab fa-html5', 95),
        ('CSS3', 'fab fa-css3-alt', 90),
        ('React', 'fab fa-react', 85),
        ('Node.js', 'fab fa-node-js', 80),
        ('Django', 'fab fa-django', 90),
        ('Git', 'fab fa-git-alt', 88),
        ('Database Management', 'fas fa-database', 85),
        ('Machine Learning', 'fas fa-brain', 85),
    ]
    
    for name, icon_class, proficiency in skills_data:
        Skill.objects.create(
            name=name,
            icon=tech_icons[icon_class],
            proficiency=proficiency
        )
    
    # Create projects
    projects_data = [
        {
            'title': 'E-Commerce Platform',
            'description': 'A full-featured e-commerce platform built with Django and React. Features include user authentication, product catalog, shopping cart, payment integration, and order management.',
            'insights': 'Implemented secure payment processing and achieved 30% improvement in page load times through optimization.',
            'demo_url': 'https://ecommerce-demo.example.com',
            'github_url': 'https://github.com/Gladwellchebelyon/ecommerce-platform'
        },
        {
            'title': 'AI Image Recognition App',
            'description': 'A machine learning application that uses deep learning to recognize and classify objects in images. Built with TensorFlow and Python.',
            'insights': 'Achieved 95% accuracy in object recognition using transfer learning with a custom-trained model.',
            'demo_url': 'https://ai-vision.example.com',
            'github_url': 'https://github.com/Gladwellchebelyon/ai-image-recognition'
        },
        {
            'title': 'Task Management System',
            'description': 'A collaborative task management system with real-time updates. Built using Django, WebSocket, and Vue.js.',
            'insights': 'Implemented real-time collaboration features that increased team productivity by 25%.',
            'demo_url': 'https://taskmaster.example.com',
            'github_url': 'https://github.com/Gladwellchebelyon/task-management'
        }
    ]
    
    for project_data in projects_data:
        Project.objects.create(**project_data)

def remove_initial_data(apps, schema_editor):
    TechIcon = apps.get_model('portfolio_app', 'TechIcon')
    Skill = apps.get_model('portfolio_app', 'Skill')
    Project = apps.get_model('portfolio_app', 'Project')
    
    Project.objects.all().delete()
    Skill.objects.all().delete()
    TechIcon.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data, remove_initial_data),
    ] 