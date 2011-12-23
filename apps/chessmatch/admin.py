from django.contrib import admin
from basic_models.admin import DefaultModelAdmin, SlugModelAdmin
from chessmatch.models import *

admin.site.register(Player, DefaultModelAdmin)


class GameAdmin(SlugModelAdmin):
    class GamePlayerInline(admin.TabularInline):
        model = GamePlayer
        extra = 0
    class GameActionInline(admin.TabularInline):
        model = GameAction
        extra = 0
    inlines = (GamePlayerInline, GameActionInline)

admin.site.register(Game, GameAdmin)