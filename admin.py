from django.contrib import admin

from showroom.models import ArtPiece, Category


@admin.register(ArtPiece)
class ArtPieceAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class ShowroomCategoryAdmin(admin.ModelAdmin):
    pass
