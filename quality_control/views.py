from django.shortcuts import render
from django.views.generic import TemplateView
from .models import BugReport
from django.views.generic import DetailView
from .models import FeatureRequest
from .forms import BugReportForm, FeatureRequestForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import BugReport, FeatureRequest
from .forms import BugReportForm, FeatureRequestForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bugs': bugs})

def add_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def add_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

# Список всех BugReports
def bug_report_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bugs': bugs})

# Создание BugReport
def bug_report_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_report_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_form.html', {'form': form})

# Обновление BugReport
def bug_report_update(request, pk):
    bug = get_object_or_404(BugReport, pk=pk)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_report_list')
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_form.html', {'form': form})

# Удаление BugReport
def bug_report_delete(request, pk):
    bug = get_object_or_404(BugReport, pk=pk)
    if request.method == 'POST':
        bug.delete()
        return redirect('quality_control:bug_report_list')
    return render(request, 'quality_control/bug_confirm_delete.html', {'bug': bug})

# Список и детали для BugReport и FeatureRequest
class BugReportListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_list.html'

class BugReportDetailView(DetailView):
    model = BugReport
    template_name = 'quality_control/bug_detail.html'

class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_form.html'
    success_url = reverse_lazy('quality_control:bug_report_list')

class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_form.html'
    success_url = reverse_lazy('quality_control:bug_report_list')

class BugReportDeleteView(DeleteView):
    model = BugReport
    template_name = 'quality_control/bug_confirm_delete.html'
    success_url = reverse_lazy('quality_control:bug_report_list')