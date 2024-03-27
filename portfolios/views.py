from django.shortcuts import render
from django.views.generic import ListView, DetailView
from showcase_module.models import WorkShowCaseModel

# Create your views here.

class PortfoliosView(ListView):
    template_name = 'portfolios/portfolios.html'
    model = WorkShowCaseModel
    context_object_name = 'works'
    ordering = ['-date']
    paginate_by = 2

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_active=True)
        return query
    


class PortfolioDetails(DetailView):
    template_name = 'portfolios/portfolio-details.html'
    model = WorkShowCaseModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    