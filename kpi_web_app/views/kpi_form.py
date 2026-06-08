from django import forms
from kpi_web_app.models import KPIMonth, KPIQuarter, KPIWeek


class KPIMonthForm(forms.ModelForm):
    class Meta:
        model = KPIMonth
        fields = ["month", "actual_value", "target_value"]


class KPIQuarterForm(forms.ModelForm):
    class Meta:
        model = KPIQuarter
        fields = ["quarter", "actual_value", "target_value"]


class KPIWeekForm(forms.ModelForm):
    class Meta:
        model = KPIWeek
        fields = ["week", "actual_value", "target_value"]


def get_forms(kpi_id, year):
    monthly_values = KPIMonth.objects.filter(kpi_id=kpi_id, year=year)
    quarterly_values = KPIQuarter.objects.filter(kpi_id=kpi_id, year=year)
    weekly_values = KPIWeek.objects.filter(kpi_id=kpi_id, year=year)
    monthly_forms = [KPIMonthForm(instance=value) for value in monthly_values]
    quarterly_forms = [KPIQuarterForm(instance=value) for value in quarterly_values]
    weekly_forms = [KPIWeekForm(instance=value) for value in weekly_values]

    return weekly_forms, monthly_forms, quarterly_forms
