from django.urls import path

from report.views import TaskPdfView
from report.views import LeaveApplicationPdfView
from report.views import SalaryReportPdfView

app_name = 'report'

urlpatterns = [
    path('task-report-pdf/<int:pk>/', TaskPdfView.as_view(), name='task_report_pdf'),
    path('leaveapplication-pdf/<int:pk>/', LeaveApplicationPdfView.as_view(), name="leaveapplication_pdf"),
    path('slarys_report/', SalaryReportPdfView.as_view(), name='salary_pdf'),
]
