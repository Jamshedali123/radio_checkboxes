from django import forms

g=[('male','MALE'),('female','FEMALE')]
c=[('python','python'),('django','django'),('api','api'),('selenium','selenium')]


class RegistrationForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.CharField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
     #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #courses=forms.MultipleChoiceField(choices=c)
    courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    
