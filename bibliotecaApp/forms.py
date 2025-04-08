from django import forms
from .models import Library, Book, User, Loan

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'
