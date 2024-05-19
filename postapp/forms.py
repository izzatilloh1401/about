from django import forms
from .models import Comments    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'website', 'msg']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({"class":"form-control"})