from django.contrib import admin
from courses.models import Category, Course
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Course
        fields = '__all__'
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'update_date', 'active']
    list_filter = ['name', 'description']
    readonly_fields = ['my_image']
    forms = CourseForm()
    def my_image(self, instance):
        if instance:
            return mark_safe(f"<img width='120' src='/static/{instance.image.name}' />")

    class Media:
        css = {'all': ('/static/css/style.css',)}

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
