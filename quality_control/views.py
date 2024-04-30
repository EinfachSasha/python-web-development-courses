from django.shortcuts import render
from django.views.generic import TemplateView
from .models import BugReport
from django.views.generic import DetailView
from .models import FeatureRequest

def index(request):
    return render(request, 'quality_control/index.html', {'title': 'Система контроля качества'})

def bug_list(request):
    return render(request, 'quality_control/bug_list.html', {'title': 'Список отчетов об ошибках'})

def feature_list(request):
    return render(request, 'quality_control/feature_list.html', {'title': 'Список запросов на улучшение'})

def bug_detail(request, bug_id):
    return render(request, 'quality_control/bug_detail.html', {'title': f'Детали бага {bug_id}'})

def feature_detail(request, feature_id):
    return render(request, 'quality_control/feature_detail.html', {'title': f'Детали улучшения {feature_id}'})

def index(request):
    return render(request, 'quality_control/index.html', {'title': 'Главная страница системы контроля качества'})

class IndexView(TemplateView):
    template_name = 'quality_control/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница системы контроля качества'
        return context

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bugs': bugs})

class BugDetailView(DetailView):
    model = BugReport
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'features': features})

class FeatureDetailView(DetailView):
    model = FeatureRequest
    template_name = 'quality_control/feature_detail.html'
    context_object_name = 'feature'