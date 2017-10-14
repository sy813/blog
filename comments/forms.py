#!/usr/bin/env python
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 125, 'rows': '5', 'placeholder': '请输入评论内容'}))

    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']
