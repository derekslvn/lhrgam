from django.shortcuts import render
from django.http import JsonResponse
from .models import Post, Comment


def get_posts(request):
    posts = Post.objects.all().values('id', 'title', 'content', 'created_at')
    return JsonResponse(list(posts), safe=False)

def get_comments(request, post_id):
    comments = Comment.objects.filter(post_id=post_id).values('id', 'content', 'created_at')
    return JsonResponse(list(comments), safe=False)

# Create your views here.
