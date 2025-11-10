from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Project, Testimonial ,Temoignage ,PhotoGalerie , CategorieGalerie
from .forms import ContactForm

def index(request):
    services = Service.objects.all()
    projects = Project.objects.all()
    temoignages = Temoignage.objects.all()
    testimonials = Testimonial.objects.all()[:5]
    categories= CategorieGalerie.objects.all()
    photos = PhotoGalerie.objects.filter(actif=True).order_by('ordre', '-date_ajout')
    for t in testimonials:
        t.range = range(t.note)
    return render(request, 'index2.html', {
        'services': services,
        'projects': projects,
        'temoignages' : temoignages ,
        'testimonials': testimonials,
        'photos': photos,
        'categories':categories
    })

def services_list(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'success': success})
