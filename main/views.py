from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306229840',
        'name': 'Wida Putri Kinasih',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)