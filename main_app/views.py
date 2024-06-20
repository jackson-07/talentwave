from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCandidateForm
from .models import Record

def home(request):
    records = Record.objects.all()
    
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
        return render(request, 'home.html', {'records': records})

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
        candidate_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'candidate_record': candidate_record})
    else:
       messages.success(request, 'You must be logged in to view candidates.')
       return redirect('home')
    
def delete_candidate(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
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
		current_record = Record.objects.get(id=pk)
		form = AddCandidateForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, 'Candidate has been updated.')
			return redirect('home')
		return render(request, 'update_candidate.html', {'form': form})
	else:
		messages.success(request, 'You must be logged in to update candidates.')
		return redirect('home')

def search_candidate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            searched = request.POST['searched']
            record = Record.objects.filter(first_name__contains=searched)
            return render(request, 'search_candidate.html', {'searched':searched, 'record': record})
        else:
            return render (request, 'search_candidate.html', {})
    else:
        messages.success(request, 'You need to be logged in to search')
        return render('home')
    