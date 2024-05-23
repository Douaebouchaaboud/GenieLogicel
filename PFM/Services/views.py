
from django.shortcuts import get_object_or_404, redirect, render
from .models import CatererService, MakeupService, Rating , DjsServices, RatingCar, RatingDjs
from .forms import RatingDjsForm, RatingForm

#Makeup-artist views 
def makeup_artist_list(request):
    makeup_artists = MakeupService.objects.all()
    return render(request, 'servicesM.html', {'makeup_artists': makeup_artists})



def makeup_artist_details(request, artist_id):
    makeup_artist = get_object_or_404(MakeupService, pk=artist_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            Rating.objects.create(makeup_service=makeup_artist, rating=rating)
            makeup_artist.update_rating(rating)
            return redirect('makeup_artist_details', artist_id=artist_id)
    else:
        form = RatingForm()
    return render(request, 'detailsM.html', {'makeup_artist': makeup_artist, 'form': form})

#Djs views 

def Djs_list(request):
    Djs = DjsServices.objects.all()
    return render(request, 'servicesDjs.html', {'Djs': Djs})

def dj_details(request, dj_id):
    dj_service = get_object_or_404(DjsServices, pk=dj_id)

    if request.method == 'POST':
        form = RatingDjsForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            RatingDjs.objects.create(Djs_services=dj_service, rating=rating)
            dj_service.update_rating(rating)
            return redirect('Djs_detail', dj_id=dj_id)
    else:
        form = RatingDjsForm()
    
    return render(request, 'detailsDj.html', {'dj_service': dj_service, 'form': form})

#traiteur
def caterer_list(request):
    caterers = CatererService.objects.all()
    return render(request, 'servicesCa.html', {'caterers': caterers})

def caterer_details(request, caterer_id):
    caterer_service = get_object_or_404(CatererService, pk=caterer_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            RatingCar.objects.create(caterer_service=caterer_service, rating=rating)
            caterer_service.update_rating(rating)
            return redirect('Traiteur_detail', caterer_id=caterer_id)
    else:
        form = RatingForm()

    return render(request, 'detailsCa.html', {'caterer_service': caterer_service, 'form': form})


