from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', '123', '&hello'],
        'obj':{
            'car':'Nissan',
            'age':20,
            'hobby':'football'
        }
    }
    return render(request, 'main/index.html', data) 

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')