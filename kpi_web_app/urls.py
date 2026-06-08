from django.urls import path, include
from .views import kpi_data_manage, home

app_name = "kpi"
urlpatterns = [
    path("home", home.home, name="home"),
    path("kpi/<str:kpi_code>/", kpi_data_manage.kpi_detail, name="kpi_detail"),
    path(
        "ajax/get-calamba-kpis/",
        kpi_data_manage.ajax_get_calamba_kpis,
        name="ajax_get_calamba_kpis",
    ),
    path("ajax/get-years/", kpi_data_manage.ajax_get_years, name="ajax_get_years"),
    path(
        "ajax/get_kpi_values/",
        kpi_data_manage.ajax_get_kpi_values,
        name="ajax_get_kpi_values",
    ),
    path(
        "edit/<int:kpi_id>/<int:year>/",
        kpi_data_manage.edit_kpi_values,
        name="edit_kpi_values",
    ),
    # path("edit-month/<int:pk>/", kpi_data_manage.edit_kpi_month, name="edit_kpi_month"),
]
