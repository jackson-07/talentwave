from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import SignUpForm, AddCandidateForm, AddJobForm
from .models import Candidate, Job, Application

def home(request):
    candidates = Candidate.objects.all()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in, welcome!')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in, please try again.')
            return redirect('home')
    else:
        return render(request, 'home.html', {'candidates': candidates})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm((request.POST))
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are registered, Welcome!')
            return redirect('home')
    else:
        form = SignUpForm()    
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})

def candidate_record(request, pk):
    if request.user.is_authenticated:
        candidate_record = Candidate.objects.get(id=pk)
        return render(request, 'candidate.html', {'candidate_record': candidate_record})
    else:
       messages.success(request, 'You must be logged in to view candidates.')
       return redirect('home')
    
def delete_candidate(request, pk):
    if request.user.is_authenticated:
        delete_record = Candidate.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, 'Candidate deleted.')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to delete candidates.')
        return redirect('home')

def add_candidate(request):
	form = AddCandidateForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == 'POST':
			if form.is_valid():
				add_candidate = form.save()
				messages.success(request, 'Candidate Added.')
				return redirect('home')
		return render(request, 'add_candidate.html', {'form': form})
	else:
		messages.success(request, 'You must be logged in to add candidates')
		return redirect('home')

def update_candidate(request, pk):
	if request.user.is_authenticated:
		current_record = Candidate.objects.get(id=pk)
		form = AddCandidateForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, 'Candidate has been updated.')
			return redirect('home')
		return render(request, 'update_candidate.html', {'form': form})
	else:
		messages.success(request, 'You must be logged in to update candidates.')
		return redirect('home')

def search(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            searched = request.POST['searched']
            candidate = Candidate.objects.filter(first_name__icontains=searched)
            job = Job.objects.filter(name__icontains=searched)
            return render(request, 'search.html', {'searched':searched, 'candidate': candidate, 'job': job})
        else:
            return render (request, 'search.html', {})
    else:
        messages.success(request, 'You need to be logged in to search')
        return render('home')
    
def jobs(request):
    if request.user.is_authenticated:
        jobs = Job.objects.all()
        return render(request, 'jobs.html', {'jobs': jobs})
    else:
       messages.success(request, 'You must be logged in to view Jobs.')
       return redirect('home')   
   
def jobs_detail(request, pk):
    if request.user.is_authenticated:
        job = get_object_or_404(Job, id=pk)
        applications = job.applications.all()
        candidates = Candidate.objects.all()
        return render(request, 'jobs_detail.html', {'job': job, 'candidates': candidates, 'applications': applications})
    else:
        messages.error(request, 'You must be logged in to view Jobs.')
        return redirect('home')
    
def delete_job(request, pk):
    if request.user.is_authenticated:
        delete_job = Job.objects.get(id=pk)
        delete_job.delete()
        messages.success(request, 'Job deleted.')
        return redirect('jobs')
    else:
        messages.success(request, 'You must be logged in to delete jobs.')
        return redirect('home')
    
def add_job(request):
	form = AddJobForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == 'POST':
			if form.is_valid():
				add_job = form.save()
				messages.success(request, 'Job Added.')
				return redirect('jobs')
		return render(request, 'add_job.html', {'form': form})
	else:
		messages.success(request, 'You must be logged in to add candidates')
		return redirect('home')

def update_job(request, pk):
	if request.user.is_authenticated:
		current_job = Job.objects.get(id=pk)
		form = AddJobForm(request.POST or None, instance=current_job)
		if form.is_valid():
			form.save()
			messages.success(request, 'Job has been updated.')
			return redirect('jobs')
		return render(request, 'update_job.html', {'form': form})
	else:
		messages.success(request, 'You must be logged in to update jobs.')
		return redirect('home')

def apply_to_job(request, job_id, candidate_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            candidate_id = request.POST.get('candidate_id')
        job = get_object_or_404(Job, id=job_id)
        candidate = get_object_or_404(Candidate, id=candidate_id)
        Application.objects.get_or_create(job=job, candidate=candidate)
        messages.success(request, 'Application successfully submitted!')
        return redirect('jobs_detail', pk=job_id)
    else:
        messages.success(request, 'You must be logged in.')
        return redirect('home')