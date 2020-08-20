from django import forms
from .models import Jasosel, Comment

class JssForm(forms.ModelForm):

    class Meta:
        model=Jasosel
        fields=('title','location','content')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].label="제목"
        self.fields['content'].label="자기소개서 내용"
        self.fields['location'].label="위치"
        
        self.fields['title'].widget.attrs.update({
            'class':'jss_title',
            'placeholder': '제목',
        })
        self.fields['content'].widget.attrs.update({
            'class':'jss_content',
            'placeholder': '본문',
        })
        self.fields['location'].widget.attrs.update({
            'class':'jss_location',
            'placeholder': '위치',
        })


class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('content',)