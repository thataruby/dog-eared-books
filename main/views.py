from django.shortcuts import render

def show_main(request):
    context = {
            'application_name': 'dog-eared-books',
            'class': 'PBD KKI',
            'name': 'Athazahra Nabila Ruby',
    }
    return render(request, "main.html", context)
