from django.db import models
from django.core.exceptions import ValidationError

class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True, blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def clean(self):
        # (No prestar un libro que ya está prestado)
        if self.active and Loan.objects.filter(book=self.book, active=True).exclude(pk=self.pk).exists():
            raise ValidationError("This book is already on loan.")

    def save(self, *args, **kwargs):
        self.clean()
        super(Loan, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.book} loaned to {self.user} on {self.loan_date}"
