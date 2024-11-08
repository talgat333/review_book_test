from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model =Review
        fields = ['name', 'email', 'rating', 'review']

        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10})
        }
    # name = forms.CharField(max_length=25)
    # email = forms.EmailField()
    # review = forms.CharField(widget=forms.Textarea)
    # rating = forms.IntegerField(min_value=1, max_value=10)



"""
 <p><input type="text" placeholder="Введите Ваше имя" name="name"></p>
 <p><input type="text" placeholder="Введите адрес электронной почты" name="email"></p>
 <p><textarea placeholder="Напишите здесь свой отзыв" cols="50" rows="5" name="review"></textarea></p>"""