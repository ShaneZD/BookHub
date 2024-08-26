from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from books.models import Book
from .models import Review
from .forms import ReviewForm

@login_required
def review_create(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form, 'book': book})