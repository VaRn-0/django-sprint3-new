from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .constants import POSTS_ON_MAIN_PAGE
from .models import Category, Post


def get_published_posts(posts=Post.objects):
    return posts.select_related(
        'author', 'category', 'location'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )


def index(request):
    return render(request, 'blog/index.html', {
        'post_list': get_published_posts()[:POSTS_ON_MAIN_PAGE]
    })


def post_detail(request, post_id):
    return render(request, 'blog/detail.html', {
        'post': get_object_or_404(get_published_posts(), pk=post_id)
    })


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': get_published_posts(category.posts),
    })
