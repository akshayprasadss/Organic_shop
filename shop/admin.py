from django.contrib import admin
from .models import Product, Review  # ✅ Import Review too
from .models import Contact

admin.site.register(Product)
admin.site.register(Review) 
admin.site.register(Contact)