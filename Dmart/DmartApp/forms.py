from django import forms  
from models import Post
from models import Employee
from platform import uname
  
class PostForm(forms.ModelForm):  
    class Meta:  
        model = Post  
        fields = "__all__"  
        
        
        
class UserForm(forms.ModelForm):  
    class Meta:  
        model = Employee
        fields = "__all__" 