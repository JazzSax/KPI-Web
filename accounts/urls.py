from django.urls import path, include
from .views import accounts


app_name = "accounts"
urlpatterns = [
    path("", accounts.account, name="account"),
    path("add-account/", accounts.add_account, name="add_account"),
    path("view-accounts/", accounts.view_accounts, name="view-accounts"),
    path("edit-account/<int:user_id>/", accounts.edit_account, name="edit-account"),
    # path("edit-month/<int:pk>/", kpi_data_manage.edit_kpi_month, name="edit_kpi_month"),
]
