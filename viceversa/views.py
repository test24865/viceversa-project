from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def revers(request):
    a = request.GET['user_text']
    reversed_text = a[::-1]
    print(type(a))
    num_words = len(a.split())
    return render(request, 'revers.html', {'user_text': a, 'reversed_text': reversed_text, 'num_words': num_words})
