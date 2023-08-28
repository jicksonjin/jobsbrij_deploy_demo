from django.shortcuts import redirect, render
from . models import *
from .forms import JobDetailsForm 
# Create your views here.

def home(request):
    jobs = job_details.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def add_job(request):
    if request.method == 'POST':
        # Extract data from the POST request.
        company_name = request.POST.get('company_name')
        job_title = request.POST.get('job_title')
        expiry_on = request.POST.get('expiry_on')
        job_description = request.POST.get('job_description')
        how_to_apply = request.POST.get('how_to_apply')
        cat_id = request.POST.get('cat')
        image = request.FILES.get('image')

        # Create a new job details instance and save it to the database.
        job_cat = job_category.objects.get(pk=cat_id)
        new_job = job_details(
            company_name=company_name,
            job_title=job_title,
            expiry_on=expiry_on,
            job_description=job_description,
            how_to_apply=how_to_apply,
            cat=job_cat,
            image=image
        )
        new_job.save()

        # Redirect to the job listing page or any other appropriate page.
        return redirect('job_list')

    # Fetch categories for populating the category dropdown.
    categories = job_category.objects.all()
    return render(request, 'add_job.html', {'cat': categories})


def add_job2(request):
    if request.method == 'POST':
        form = JobDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobDetailsForm()

    return render(request, 'add_job2.html', {'form': form})



def index(request):
    job_list = job_details.objects.all()
    context = {'job_list': job_list }
    return render(request, 'index.html', context)
