from app import admin, db
from apps.admin.models.tenants import Tenants
from apps.admin.tenant_view import TenantView


def load_admin_views():
    # from app import dbfl
    admin.add_view(TenantView(Tenants, db.session))
