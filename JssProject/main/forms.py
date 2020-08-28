from django import forms
from .models import Jasosel, Comment

class JssForm(forms.ModelForm):

    class Meta:
        model=Jasosel
        fields=('title','location_si','location_gu','content')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].label="제목"
        self.fields['content'].label="자기소개서 내용"
        self.fields['location_si'].label="시"
        self.fields['location_gu'].label="구"
        
        self.fields['title'].widget.attrs.update({
            'class':'jss_title',
            'placeholder': '제목',
        })
        self.fields['content'].widget.attrs.update({
            'class':'jss_content',
            'placeholder': '본문',
        })
        self.fields['location_si'].widget.attrs.update({
            'class':'jss_location',
            'placeholder': '시',
        })
        self.fields['location_gu'].widget.attrs.update({
            'class':'jss_location_gu',
            'placeholder': '구',
        })
        if self.fields['location_si']=='Seoul':
            location_gu=forms.ChoiceField(chocies=[('GangnamGu','GangnamGu'),('MapoGu','MapoGu')])
        if self.fields['location_si']=='Daegu':
            location_gu=forms.ChocieField(chocies=[('BukGu','BukGu'),('SuseongGu','SuseongGu')])

class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('content',)