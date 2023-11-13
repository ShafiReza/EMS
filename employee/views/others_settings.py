from django.db.models import Sum
# Generic Classes
from django.views.generic import ListView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from employee.permission import EmployeePassesTestMixin

# Models
from authority.models import MonthlyHoliDay
from authority.models import LeaveType
from authority.models import LeaveApplication

# Filters
from authority.filters import MonthlyHoliDayFilter


class EmployeeMonthlyHolidayView(LoginRequiredMixin, EmployeePassesTestMixin, ListView):
    model = MonthlyHoliDay
    queryset = MonthlyHoliDay.objects.filter(is_active=True)
    filterset_class = MonthlyHoliDayFilter
    template_name = 'employee/employee_holiday.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Monthly Holiday"
        context["holidays"] = self.filterset_class(self.request.GET, queryset=self.queryset)

        return context


class EmployeeYearlyLeaveView(LoginRequiredMixin, EmployeePassesTestMixin, ListView):
    model = LeaveType
    template_name = 'employee/yearly_leave.html'

    def get_context_data(self, **kwargs):
        total_leave = LeaveType.objects.filter( is_active=True).aggregate(Sum('permited_days'))['permited_days__sum']
        my_total_leave = LeaveApplication.objects.filter(is_active= True, approved_status=True).count()
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Leave Type"
        context["leaves"] = LeaveType.objects.filter(is_active=True)
        context["total_leaves"] = total_leave
        context["my_total_leaves"] = my_total_leave
        context["my_leaves_left"] = total_leave-my_total_leave
        return context
