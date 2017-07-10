from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView

from showroom.models import ArtPiece, Category


class CategoryListView(ListView):
    model = Category
    template = 'category_list.html'

class ArtPieceListView(ListView):
    model = ArtPiece
    template = 'art_piece_list.html'

    def get_queryset(self):
        qs = super(ArtPieceListView, self).get_queryset()
        cat_id = self.kwargs.get('cat_id', None)
        if cat_id:
            qs = qs.filter(category__id=cat_id)
        return qs
