import django_filters
from .models import *
from django_filters.filters import CharFilter, forms, MultipleChoiceFilter, ChoiceFilter, ModelChoiceFilter, ModelMultipleChoiceFilter


class PostFilter(django_filters.FilterSet):
    title = CharFilter(widget=forms.TextInput(attrs={
                       "class": "form-control", "placeholder": "ady"}), field_name="title", lookup_expr="icontains")
    category = ModelChoiceFilter(field_name="category", empty_label="Kategoriýa", queryset=Category.objects.all(), widget=forms.Select(
        attrs={"class": "form-control"}))

    # tagList = ModelMultipleChoiceFilter(field_name="tagList", queryset=Tag.objects.all(
    #     ), widget=forms.CheckboxSelectMultiple(attrs={"class": "form-group form-control"}))


class Meta:
    model = Post
    fields = ["title", "tagList"]
    exclude = ["image", "like", "seen", "share"]
