from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Order, Comment
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.http import JsonResponse
import json
from .forms import CommentForm
from users.models import Profile

class HomeView(ListView):
    model = Book
    template_name = 'home.html'


class BooksDetailView(DetailView):
    model = Book
    template_name = 'detail.html'
    http_method_names = ['post', 'get']

    def get(self, request, *args, **kwargs):
        book = Book.objects.get(id = self.kwargs['pk'])
        comments = Comment.objects.filter(book=book, approved_comment=True)
        new_comment = None

        comment_form = CommentForm()

        return render(request, self.template_name, {'book': book, 'comments': comments,
                                                    'new_comment': new_comment,'comment_form': comment_form})

    def post(self, request, *args, **kwargs):
        book = Book.objects.get(id=self.kwargs['pk'])
        comments = Comment.objects.filter(book=book, approved_comment=True)
        new_comment = None

        comment_form = CommentForm(data=self.request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.author = self.request.user
            new_comment.save()

        return render(request, self.template_name, {'book': book, 'comments': comments,
                                                    'new_comment': new_comment, 'comment_form': comment_form, 'book': book})



class SearchResultsListView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
        Q(name__icontains=query) | Q(author__icontains=query)
        )

class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url = 'login'


def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    product = Book.objects.get(id=body['productId'])
    Order.objects.create(
        product=product
    )
    return JsonResponse('Payment completed!', safe=False)