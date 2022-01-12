from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import User
 
class UserAdmin(UserAdmin):
    model  = User
    fields = ("email",)
    list_filter = ("email",)
    list_display = ("email",)
    
 
# Now register the new UserAdmin...
admin.site.register(User)

 