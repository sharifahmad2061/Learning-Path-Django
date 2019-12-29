from django.shortcuts import render
from django.http import Http404

from .models import Job


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/index.html', {'jobs': jobs})


def job_detail(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        print(job)
    except Job.DoesNotExist:
        raise Http404('Job Not Found')
    return render(request, 'jobs/job_detail.html', {'job': job})
