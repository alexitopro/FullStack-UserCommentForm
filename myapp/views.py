from django.shortcuts import render

# Create your views here.
from myapp.forms import CommentForm
from .models import UserComments
from django.http import JsonResponse

def form_view(request):
    #rendering and processing form data
    form = CommentForm()

    if request.method == 'POST':
        #updates the form with the POST data
        form = CommentForm(request.POST)
        if form.is_valid():
            #clean data
            cd = form.cleaned_data
            #send data to the model
            uc = UserComments(
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                comment = cd['comment']
            )
            #update the model data
            uc.save()
            return JsonResponse({'message': 'success'})

    #return as dictionary
    return render(request, 'blog.html', {'form': form})