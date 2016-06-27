from django.contrib import admin
from customer_api.models import Customer
from django.utils.translation import ugettext, ugettext_lazy as _


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Personal info'), {
         'fields': ('first_name', 'middle_name', 'last_name', 'occupation', 'dob', 'age', 'marriage_anniversary', 'agriculture_status', 'purpose_of_buying')}),
        (_('Contact Details'), {'fields': ('email', 'mobile', 'alternet_mobile', 'address1',
                                       'address2', 'pin_code', 'photo')}),
        (_('Nominee Details'), {'fields': ('nominee_name', 'nominee_address', 'nominee_email', 'nominee_mobile',
            'nominee_alternet_mobile', 'nominee_photo', 'nominee_dob', 'nominee_age', 'nominee_occupation', 'relation' )})
    )

admin.site.register(Customer, CustomerAdmin)
