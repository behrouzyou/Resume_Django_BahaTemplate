from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.db.models import Q
from django.shortcuts import reverse
from .models import Post, BlogCategory, Tag
from .forms import CommentForm, SearchForm


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6  # صفحه بندی

    def get_queryset(self):
        queryset = Post.objects.filter(is_active=True)

        # جستجو
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query)
            )

        # فیلتر بر اساس دسته بندی
        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        # فیلتر بر اساس تگ
        tag_slug = self.request.GET.get('tag')
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # داده‌های مورد نیاز سایدبار
        context['categories'] = BlogCategory.objects.all()
        context['recent_posts'] = Post.objects.filter(is_active=True).order_by('-created_at')[:3]
        context['tags'] = Tag.objects.all()
        context['search_form'] = SearchForm(self.request.GET)
        return context


class BlogDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'blog/blog_single.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.all()
        context['recent_posts'] = Post.objects.filter(is_active=True).order_by('-created_at')[:3]
        context['tags'] = Tag.objects.all()
        context['comments'] = self.object.comments.filter(is_approved=True, parent__isnull=True)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)