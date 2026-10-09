from django.shortcuts import render

# Create your views here.
from ..models.offre import Offre


def liste_offres(request):
    offres = Offre.objects.select_related("entreprise").prefetch_related("competences")  # noqa: F841
    return render(
        request,
        "stages/liste_offres.html",
        {"offres": Offre.objects.all()},
    )
