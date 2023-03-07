from django.shortcuts import render, redirect
from .models import Articals
from .forms import ArticalsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news=Articals.objects.order_by('-data')
    return render(request, 'news/news_home.html', {'news':news})
#Показывает и сортирует домашнию страницу статьей

class NewsDetailView(DetailView):
    model = Articals
    template_name = 'news/details_view.html'
    context_object_name = 'article'
#класс который обрабатывает html файл и показывает его

class NewsUpdateView(UpdateView):
    model = Articals
    template_name = 'news/create.html'
    form_class = ArticalsForm

class NewsDeleteView(DeleteView):
    model =Articals
    success_url = '/news/'
    template_name = 'news/news_delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticalsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена не верно'

    form = ArticalsForm()

    data = {
        'form': form,
        'error':error
    }
    
    return render(request, 'news/create.html', data)
