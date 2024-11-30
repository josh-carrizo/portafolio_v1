from django.contrib import admin
from .models import Project, Experience, Education, Contact

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'description')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'description')   

@admin.register(Education)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'place_studies', 'start_date', 'end_date', 'description')   

admin.site.register(Contact)          