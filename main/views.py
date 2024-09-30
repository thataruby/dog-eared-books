from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from main.forms import BookEntryForm
from main.models import BookEntry
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse


@login_required(login_url='/login')
def show_main(request):
    book_entries = BookEntry.objects.filter(user=request.user)

    context = {
        'application_name': 'dog-eared-books',
        'class': 'PBP KKI',
        'name': request.user.username,
        'book_entries': book_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_book_entry(request):
    form = BookEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        book_entry = form.save(commit=False)
        book_entry.user = request.user
        book_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_book_entry.html", context)

def show_xml(request):
    data = BookEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BookEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = BookEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = BookEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_book(request, id):
    book = BookEntry.objects.get(pk = id)

    form = BookEntryForm(request.POST or None, instance=book)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_book.html", context)

def delete_book(request, id):
    # Get book based on id
    book = BookEntry.objects.get(pk = id)
    # Delete book
    book.delete()
    # Return to home page
    return HttpResponseRedirect(reverse('main:show_main'))