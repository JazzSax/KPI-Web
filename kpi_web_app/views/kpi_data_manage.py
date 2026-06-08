from kpi_web_app.models import KPI, CalambaKPI, KPIMonth, KPIQuarter, KPIWeek
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .kpi_form import KPIMonthForm, KPIQuarterForm, KPIWeekForm, get_forms

from django.forms import modelformset_factory


# Return all kpi for the dropdown
def get_all_kpi_names():
    return KPI.objects.all().values("kpi_name", "kpi_code")


# Return all calamba kpi based on chosen kpi
def get_calamba_kpis_by_kpi_code(kpi_code):
    return CalambaKPI.objects.filter(kpi_code__kpi_code=kpi_code).values(
        "calamba_kpi", "kpi_id"
    )


# Return all the years
def get_years_by_kpi_id(kpi_id):
    return (
        KPIMonth.objects.filter(kpi_id=kpi_id).values_list("year", flat=True).distinct()
    )


# Request all the calamba kpi based on kpi
def ajax_get_calamba_kpis(request):
    kpi_code = request.GET.get("kpi_code")
    calamba_kpis = get_calamba_kpis_by_kpi_code(kpi_code)
    print("calamba kpis", calamba_kpis)
    return JsonResponse(list(calamba_kpis), safe=False)


# Request all the years based on calamba kpi
def ajax_get_years(request):
    kpi_id = request.GET.get("kpi_id")
    years = get_years_by_kpi_id(kpi_id)
    return JsonResponse(list(years), safe=False)


def ajax_get_kpi_values(request):
    kpi_id = request.GET.get("kpi_id")
    calamba_kpi = request.GET.get("calamba_kpi")
    year = request.GET.get("year")

    weekly_forms, monthly_forms, quarterly_forms = get_forms(calamba_kpi, year)

    # Prepare data for JSON response
    data = {
        "weekly_forms": [
            {
                "week": form.instance.week,
                "actual_value": form.instance.actual_value,
                "target_value": form.instance.target_value,
            }
            for form in weekly_forms
        ],
        "monthly_forms": [
            {
                "month": form.instance.month,
                "actual_value": form.instance.actual_value,
                "target_value": form.instance.target_value,
            }
            for form in monthly_forms
        ],
        "quarterly_forms": [
            {
                "quarter": form.instance.quarter,
                "actual_value": form.instance.actual_value,
                "target_value": form.instance.target_value,
            }
            for form in quarterly_forms
        ],
    }

    return JsonResponse(data)


def edit_kpi_values(request, kpi_id, year):
    # Fetch all KPI values for the given kpi_id and year
    kpi = CalambaKPI.objects.filter(kpi_id=kpi_id).values("kpi_code").first()
    monthly_values = KPIMonth.objects.filter(kpi_id=kpi_id, year=year)
    quarterly_values = KPIQuarter.objects.filter(kpi_id=kpi_id, year=year)
    weekly_values = KPIWeek.objects.filter(kpi_id=kpi_id, year=year)

    if request.method == "POST":
        # Update monthly values
        for value in monthly_values:
            value.actual_value = request.POST.get(
                f"month_actual_{value.pk}", value.actual_value
            )
            value.save()

        # Update quarterly values
        for value in quarterly_values:
            value.actual_value = request.POST.get(
                f"quarter_actual_{value.pk}", value.actual_value
            )
            value.save()

        # Update weekly values
        for value in weekly_values:
            value.actual_value = request.POST.get(
                f"week_actual_{value.pk}", value.actual_value
            )
            value.save()

        return redirect(
            "kpi_detail", kpi_code=kpi["kpi_code"]
        )  # Redirect to KPI detail page after saving

    return render(
        request,
        "kpi/edit_kpi_value.html",
        {
            "monthly_values": monthly_values,
            "quarterly_values": quarterly_values,
            "weekly_values": weekly_values,
        },
    )


def kpi_detail(request, kpi_code="OTM_DLV"):
    kpi_names = get_all_kpi_names()
    calamba_kpis = CalambaKPI.objects.filter(kpi_code__kpi_code=kpi_code).values(
        "calamba_kpi", "kpi_id"
    )
    first_calamba_kpi = calamba_kpis.first()
    years = get_years_by_kpi_id(first_calamba_kpi["kpi_id"])
    first_year = years.first()
    kpi_id = first_calamba_kpi["kpi_id"]
    weekly_forms, monthly_forms, quarterly_forms = get_forms(kpi_id, first_year)
    return render(
        request,
        "kpi/kpi_detail.html",
        {
            "kpi_names": kpi_names,
            "calamba_kpis": calamba_kpis,
            "years": years,
            "monthly_forms": monthly_forms,
            "quarterly_forms": quarterly_forms,
            "weekly_forms": weekly_forms,
        },
    )


# def edit_kpi_month(request, pk):
#     instance = KPIMonth.objects.get(pk=pk)
#     form = KPIMonthForm(request.POST or None, instance=instance)

#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect(
#             "kpi_detail", kpi_code=instance.kpi_id.kpi_code
#         )  # Redirect to KPI detail page after saving

#     return render(request, "kpi/edit_kpi_month.html", {"form": form})
