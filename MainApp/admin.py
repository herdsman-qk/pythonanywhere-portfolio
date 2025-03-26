from django.contrib import admin
from .models import Profile, Skill, Education, Experience, Project, ExperienceItem, MyMail


# Custom Admin for Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'city', 'title', 'is_active')  # Columns to display in list view
    search_fields = ('first_name', 'last_name', 'email')  # Enable search for these fields
    list_filter = ('city',)  # Enable filtering by city

    # Custom Admin for Skill


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')  # Columns to display in list view
    search_fields = ('name',)  # Enable search for skill name


# Custom Admin for Education
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'university', 'entered_date', 'graduation_date')  # Columns to display
    search_fields = ('degree', 'university')  # Enable search for degree and university


class ExperienceItemInline(admin.StackedInline):
    model = ExperienceItem
    extra = 0

# Custom Admin for Experience
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'entered_date', 'finished_date', 'location')  # Columns to display
    search_fields = ('position', 'company', 'location')  # Enable search for position and company
    inlines = [ExperienceItemInline]


class ExperienceItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'experience')
    search_fields = ('description',)

# Custom Admin for Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'summary', 'github_url')  # Columns to display in list view
    search_fields = ('title', 'github_url')  # Enable search for title and URL

class MyMailAdmin(admin.ModelAdmin):
    list_display = ('from_name', 'from_email', 'subject', 'message')
    search_fields = ('from_name', 'from_email', 'subject', 'message')

# Register the models
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ExperienceItem, ExperienceItemAdmin)
admin.site.register(MyMail, MyMailAdmin)
