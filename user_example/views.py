from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import requests


headers = {
    'X-AYLIEN-TextAPI-Application-Key': 'APPLICATION_KEY',
    'X-AYLIEN-TextAPI-Application-ID': 'APPLICATION_ID'}


@login_required
def home(request):

    if request.method == "POST":
        url = request.POST['search'].strip()
        return redirect(f'/sentiment/?url={url}')

    return render(request, 'home.html')


@login_required
def sentiment(request):

    if request.method == "POST":
        url = request.POST['search'].strip()
        return redirect(f'/sentiment/?url={url}')

    url = request.GET['url'].strip()

    response = requests.get(
        f'https://api.aylien.com/api/v1/sentiment?url={url}', headers=headers)
    data = response.json()

    data['url'] = url

    return render(request, 'result/sentiment.html', {'data': data})


@login_required
def classification(request):

    if request.method == "POST":
        url = request.POST['search'].strip()
        return redirect(f'/classification/?url={url}')

    url = request.GET['url'].strip()

    response = requests.get(
        f'https://api.aylien.com/api/v1/classify?url={url}', headers=headers)
    data = response.json()

    data['url'] = url

    return render(request, 'result/classification.html', {'data': data})


@login_required
def concepts(request):

    if request.method == "POST":
        url = request.POST['search'].strip()
        return redirect(f'/concepts/?url={url}')

    url = request.GET['url'].strip()

    response = requests.get(
        f'https://api.aylien.com/api/v1/concepts?url={url}', headers=headers)
    data = response.json()
    data['url'] = url

    return render(request, 'result/concepts.html', {'data': data})


@login_required
def entities(request):

    if request.method == "POST":
        url = request.POST['search'].strip()
        return redirect(f'/entities/?url={url}')

    url = request.GET['url'].strip()

    response = requests.get(
        f'https://api.aylien.com/api/v1/entities?url={url}', headers=headers)
    data = response.json()
    data['url'] = url

    return render(request, 'result/entities.html', {'data': data})


@login_required
def summary(request):

    if request.method == "POST":
        url = request.POST['search'].strip()
        return redirect(f'/summary/?url={url}')

    url = request.GET['url'].strip()

    response = requests.get(
        f'https://api.aylien.com/api/v1/summarize?url={url}', headers=headers)
    data = response.json()
    data['url'] = url

    return render(request, 'result/summary.html', {'data': data})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
