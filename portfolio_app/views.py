from django.shortcuts import render
from .models import Project, Contact, Skill

# View for the homepage
def homepage(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    context = {
        'projects': projects,
        'skills': skills,
        'linkedin_url': 'https://www.linkedin.com/in/gladwell-chepkorir-a29a79238',  # Added full URL
        'github_url': 'https://github.com/Gladwellchebelyon',
    }
    return render(request, 'portfolio_app/homepage.html', context)

# If you want to create a separate contact page
def contact(request):
    return render(request, 'portfolio_app/contact.html')  # Ensure you have a contact.html template
