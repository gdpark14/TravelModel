from django import forms
from .models import Jasosel, Comment,City

class JssForm(forms.ModelForm):

    class Meta:
        model=Jasosel
        fields=('title','country','city','content')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].label="제목"
        self.fields['content'].label="자기소개서 내용"

        
        self.fields['title'].widget.attrs.update({
            'class':'jss_title',
            'placeholder': '제목',
        })
        self.fields['content'].widget.attrs.update({
            'class':'jss_content',
            'placeholder': '본문',
        })
        self.fields['city'].queryset=City.objects.none()

        if 'country' in self.data:
            try:
                country_id=int(self.data.get('country'))
                self.fields['city'].queryset=City.objects.filter(country_id=country_id)
            except:
                pass



class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('content',)