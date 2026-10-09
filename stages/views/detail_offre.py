from django.shortcuts import get_object_or_404, render

from ..models.offre import Offre


def detail_offre(request, pk):
    offre = get_object_or_404(Offre, pk=pk)
    return render(
        request, 
        "stages/detail_offre.html", 
        {"offre": offre}
    )
