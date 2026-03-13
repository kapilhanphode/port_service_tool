from django.contrib.admin import AdminSite

class PortAdminSite(AdminSite):
    site_header = "Port Service Tool Admin"
    site_title = "Port Service Tool"
    index_title = "Dashboard"

    def get_app_list(self, request):
        """
        Custom app grouping for the sidebar:
        - Masters: Services + Vessels
        - Companies
        - Accounts
        """
        app_dict = self._build_app_dict(request)
        app_list = []

        # Models to go under "Masters"
        masters_models = ['service', 'vessel', 'rfq', 'quotation']  # lowercase model names
        masters_block = []

        for app_label, app in app_dict.items():
            # Extract models for Masters
            for m in app['models']:
                if m['object_name'].lower() in masters_models:
                    masters_block.append(m)

        # Remove Masters models from original apps
        for app in app_dict.values():
            app['models'] = [m for m in app['models'] if m['object_name'].lower() not in masters_models]

        # Add Masters block if it has models
        if masters_block:
            app_list.append({
                'name': 'Masters',
                'app_label': 'masters',
                'app_url': '',
                'has_module_perms': True,
                'models': masters_block
            })

        # Add remaining apps
        for app in app_dict.values():
            if app['models']:
                app_list.append(app)

        return app_list

# Instantiate the custom admin
port_admin = PortAdminSite(name='port_admin')