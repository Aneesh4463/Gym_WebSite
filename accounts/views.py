
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm


class OwnerLoginView(View):

    def get(self, request, *args, **kwargs):

        form = AuthenticationForm()

        return render(request,'accounts/owner_login.html',{'form': form})

    def post(self, request, *args, **kwargs):

        form = AuthenticationForm(request,data=request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']

            password = form.cleaned_data['password']

            user = authenticate(request,username=username,password=password)

            if user is not None and user.is_staff:

                login(request, user)

                return redirect('owner_dashboard')

            form.add_error(None,'You are not authorized to access the owner panel.')

        return render(request,'accounts/owner_login.html',{'form': form})


class OwnerRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('owner_login')

        if not request.user.is_staff:
            return redirect('owner_login')

        return super().dispatch(request, *args, **kwargs)


class OwnerDashboardView(OwnerRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        
        return render(request, 'accounts/owner_dashboard.html')


class OwnerLogoutView(View):

    def post(self, request, *args, **kwargs):

        logout(request)
        
        return redirect('owner_login')

