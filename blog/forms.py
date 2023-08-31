from django import forms
from blog.models import Post, Category, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["picture","title","content",]


    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"