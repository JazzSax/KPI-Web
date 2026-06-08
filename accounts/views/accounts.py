from django.shortcuts import render, redirect, get_object_or_404
from ..forms import UserCreationForm, UserEditForm
from ..models import Roles, Users


def account(request):
    return render(request, "accounts/account_view.html")


def view_accounts(request):
    return render(request, "accounts/account_view.html")


def add_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            # Create a role with the selected permissions
            role = Roles.objects.create(
                role_name=f"{user.firstname} {user.lastname} Custom Role",
                can_view=form.cleaned_data["can_view"],
                can_edit=form.cleaned_data["can_edit"],
                can_delete=form.cleaned_data["can_delete"],
                otm_dlv=form.cleaned_data["otm_dlv"],
                eqp_util=form.cleaned_data["eqp_util"],
                cst_cmp=form.cleaned_data["cst_cmp"],
                exc=form.cleaned_data["exc"],
                cst_rst=form.cleaned_data["cst_rst"],
                ops_b1f1_ass_yld=form.cleaned_data["ops_b1f1_ass_yld"],
                sft=form.cleaned_data["sft"],
                cost=form.cleaned_data["cost"],
            )
            user.roles.add(role)
            return redirect("view-accounts")  # Use the correct URL name here
    else:
        form = UserCreationForm()

    return render(request, "accounts/add_account.html", {"form": form})


def edit_account(request, user_id):
    user = get_object_or_404(Users, employee_id=user_id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("view-accounts")  # Redirect to the view that lists accounts
    else:
        form = UserEditForm(instance=user)

    return render(request, "accounts/edit_account.html", {"form": form, "user": user})
