from flask_admin.contrib.sqla import ModelView


class TenantView(ModelView):
    column_list = ['object_id', 'object_name', 'object_address', 'tenant_name', 'apartment_number', 'rent_start',
                   'rent_end', 'rent_price']
    column_filters = ['object_id', 'object_name', 'object_address', 'tenant_name', 'apartment_number', 'rent_start',
                      'rent_end', 'rent_price']
    form_columns = ['object_id', 'object_name', 'object_address', 'tenant_name', 'apartment_number', 'rent_start',
                    'rent_end', 'rent_price']
