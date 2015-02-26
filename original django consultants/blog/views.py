from django.shortcuts import render
from forms import BulletinForm

# Create your views here.
from blog.models import Blog, Bulletin, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
import datetime



def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5],
        'bulletins': Bulletin.objects.all(),
    })


def view_post(request, slug):
    return render_to_response('blog/view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })


def create_post(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BulletinForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data['title']
            location = form.cleaned_data['location']
            date = datetime.date.today()
            author = form.cleaned_data['author']
            body = form.cleaned_data['body']
            bulletin = Bulletin.objects.create(title=title,
                                           location=location,
                                           date=date,
                                           author=author,
                                           body=body)
            bulletin.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/blog/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BulletinForm()

    return render(request, 'blog/create_post.html', {'form': form})

#def search_form(request):
#    return render(request, 'search_form.html')

def search_form(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            bulletin = Bulletin.objects.filter(title__icontains=q)
            return render(request, 'blog/search_results.html',
                {'Bulletin': bulletin, 'query': q})
    return render(request, 'blog/search_form.html',
        {'error': error})