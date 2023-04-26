from django.contrib import admin
from .models import EmployeeRefer,PDFFile

  
admin.site.register(EmployeeRefer)


from .models import OTP

# Register the OTP model with the admin site
admin.site.register(OTP)
admin.site.register(PDFFile)