from django import forms
from .models import Users, Roles


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    # Checkbox fields for each permission
    can_view = forms.BooleanField(required=False, label="Can View")
    can_edit = forms.BooleanField(required=False, label="Can Edit")
    can_delete = forms.BooleanField(required=False, label="Can Delete")
    otm_dlv = forms.BooleanField(required=False, label="OTM Delivery")
    eqp_util = forms.BooleanField(required=False, label="Equipment Utilization")
    cst_cmp = forms.BooleanField(required=False, label="Cost Comparison")
    exc = forms.BooleanField(required=False, label="Execution")
    cst_rst = forms.BooleanField(required=False, label="Cost Restriction")
    ops_b1f1_ass_yld = forms.BooleanField(required=False, label="Ops B1F1 Ass Yld")
    sft = forms.BooleanField(required=False, label="Safety")
    cost = forms.BooleanField(required=False, label="Cost")

    class Meta:
        model = Users
        fields = [
            "employee_id",
            "email",
            "firstname",
            "lastname",
            "contact_number",
            "password",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")

        return cleaned_data


class UserEditForm(forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(
        queryset=Roles.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Roles",
        required=False,
    )

    class Meta:
        model = Users
        fields = [
            "employee_id",
            "email",
            "firstname",
            "lastname",
            "contact_number",
            "roles",
        ]

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        # Prepopulate the roles field with the user's current roles
        if self.instance:
            self.fields["roles"].initial = self.instance.roles.all()
