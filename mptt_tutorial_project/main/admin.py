from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Genre


admin.site.register(Genre, DraggableMPTTAdmin,
                    list_display=('tree_actions', 'id', 'name', 'parent'), list_display_links=('name',))
