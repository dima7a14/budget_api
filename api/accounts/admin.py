from django.contrib import admin

from .models import Account, Transaction, Category


class TransactionInline(admin.TabularInline):
    model = Transaction
    min_num = 0
    max_num = 10
    extra = 0


class AccountAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    readonly_fields = ('created_at', 'updated_at')
    inlines = [TransactionInline]


class TransactionAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    readonly_fields = ('created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category, CategoryAdmin)
