from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import forms, HiddenInput, ModelForm

from mainapp.models import ProductCategory, Product


class AgeValidationMixin:
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and age < 18:
            raise forms.ValidationError('Вы слишком молоды!')
        return age


class AdminShopUserCreateForm(UserCreationForm, AgeValidationMixin):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name',
                  'password1', 'password2', 'email', 'age', 'avatar',
                  'is_staff', 'is_superuser', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''
            if field_name == 'password':
                field.widget = HiddenInput()


class AdminShopUserUpdateForm(UserChangeForm, AgeValidationMixin):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password',
                  'email', 'age', 'avatar',
                  'is_staff', 'is_superuser', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''
            if field_name == 'password':
                field.widget = HiddenInput()


class AdminProductCategoryUpdateForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AdminProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'category':
                field.widget = HiddenInput()
