from django import forms
from .models import Posting

class PostingForm(forms.ModelForm):
    
    class Meta:
        model = Posting
        # modelから入力フォームを生成する対象のフィールドをタプル形式で指定
        fields = ('name','message')
        # 使わないフィールドを定義するパターン。上と同義
        # excludes = ('created_at')
        widgets = {
            'name': forms.TextInput(attrs={'size': 40}),
            'message': forms.Textarea(attrs={'cols':80, 'rows':20})
        }
