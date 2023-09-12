from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}  # '' 表示不要對該欄位建立 label
