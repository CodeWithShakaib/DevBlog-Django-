from django.shortcuts import render,HttpResponse
from .models import Articles,Author
# Create your views here.

def index(request):
    all_entries = Articles.objects.all()
    data = []
    for obj in all_entries:
        data.append({'author_name':obj.author.full_name,
                    'author_email':obj.author.email,
                    'name':obj.name,
                    'image':obj.image,
                    'published_date':obj.published_date,
                    'time':obj.time_read,
                    'content':obj.content[:300]})

    print(all_entries[2].id)
    
    return render(request,'index.html',{'articles':data})


def blogPost(request):
    return render(request,'blogPost.html')