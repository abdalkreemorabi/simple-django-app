from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView

from jobs.forms import JobSearchForm
from jobs.models import Job


class HomeView(TemplateView):
    template_name = "home.html"


class JobView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'jobs/job_search.html'
    context_object_name = 'jobs'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        form = JobSearchForm(self.request.GET or None)

        if form.is_valid():
            job_title = form.cleaned_data.get('job_title')
            if job_title:
                queryset = queryset.filter(title__icontains=job_title)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = JobSearchForm(self.request.GET or None)
        return context
