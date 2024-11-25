from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser



class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('shop:all_products')

    def form_valid(self, form):
        # Save the new user
        response = super().form_valid(form)

        # Add user to the Customer group
        customer_group, created = Group.objects.get_or_create(name='Customer')
        self.object.groups.add(customer_group)

        # Log the user in after signup
        login(self.request, self.object)
        
        return response