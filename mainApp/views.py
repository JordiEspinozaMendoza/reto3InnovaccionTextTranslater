from django.shortcuts import render
from .models import Photo
from .forms import PhotoForm
from .text import textTranlater
# Create your views here.


def home(request):
    areResults = False
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            image = Photo.objects.last()
            url = image.image.url
            predictionResults = textTranlater(url)
            areResults = True
            context = {'form': PhotoForm(),
                       'results': predictionResults, 'areResults': areResults}
            return render(request, "index.html", context)
    else:
        form = PhotoForm()

    context = {'form': form, 'areResults': areResults}
    return render(request, 'index.html', context)
