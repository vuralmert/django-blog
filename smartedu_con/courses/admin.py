from django.contrib import admin
from .models import Course, Category, Tag
from teachers.models import Teacher



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','teacher', 'available', 'date')
    list_filter = ('available', 'teacher', 'category')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

