from django import forms
from .models import Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=("rating","title","comment")
        widgets={"rating":forms.Select(choices=[(i,f"{i} / 5") for i in range(1,6)])}
