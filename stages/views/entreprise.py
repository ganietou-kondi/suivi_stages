from django.shortcuts import get_object_or_404, render

# Create your views here.
from ..models.entreprise import Entreprise


def liste_entreprises(request):
    return render(
        request,
        "stages/liste_entreprises.html",
        {"entreprises": Entreprise.objects.all()},
    )



def detail_entreprise(request, pk):
    entreprise = get_object_or_404(Entreprise, pk=pk) 
    return render(
        request, 
        "stages/detail_entreprise.html", 
        {"entreprise": entreprise}
    )
