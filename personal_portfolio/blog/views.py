from django.shortcuts import render
from django.views.generic import DetailView

from .models import Post


def blog(request):
    posts = Post.objects.order_by('-date')

    context = {
        'title': 'Блог',
        'posts': posts
    }

    return render(request, 'blog/blog.html', context=context)


class PostDetail(DetailView):
    """Просмотр поста"""
    model = Post
    template_name = 'blog/PostDetail.html'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        """Заполнение словаря context"""
        context = super().get_context_data(**kwargs)
        context['title'] = context['object']
        return context
