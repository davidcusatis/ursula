from django.utils.translation import ugettext_lazy as _

import horizon

# expose host aggregates to cloud_admin
admin_dashboard = horizon.get_dashboard("admin")

# default permissions for admin_dashboard _should_ be ('openstack.roles.admin',)
# so we want to append to the first item because of this undocumented
#       horizon slickness
# https://github.com/openstack/django_openstack_auth/blob/master/openstack_auth/user.py#L376
# (('openstack.roles.admin', 'openstack.roles.cloud_admin',),) == logcal OR on
#       the first tuple
permissions = list(getattr(admin_dashboard, 'permissions', []))
permissions[0] = (permissions[0],) + ('openstack.roles.cloud_admin',)

# set admin dashboard visible to both admin, and cloud_admin
admin_dashboard.permissions = tuple(permissions)

#expose aggregates to cloud_admin
aggregates = admin_dashboard.get_panel('aggregates')
aggregates_permissions = list(getattr(aggregates, 'permissions', []))
# aggregates perms already has admin, it's a similar case as with the dashboard
aggregates_permissions[0] = (aggregates_permissions[0],) + ('openstack.roles.cloud_admin',)
aggregates.permissions = tuple(aggregates_permissions)

# hide defaults from cloud_admin
defaults = admin_dashboard.get_panel('defaults')
defaults_permissions = list(getattr(defaults, 'permissions', []))
defaults_permissions.append('openstack.roles.admin')
defaults.permissions = tuple(defaults_permissions)

# hide flavors from cloud_admin
flavors = admin_dashboard.get_panel('flavors')
flavors_permissions = list(getattr(flavors, 'permissions', []))
flavors_permissions.append('openstack.roles.admin')
flavors.permissions = tuple(flavors_permissions)

# hide images from cloud_admin
images = admin_dashboard.get_panel('images')
images_permissions = list(getattr(images, 'permissions', []))
images_permissions.append('openstack.roles.admin')
images.permissions = tuple(images_permissions)

# hide info from cloud_admin
info = admin_dashboard.get_panel('info')
info_permissions = list(getattr(info, 'permissions', []))
info_permissions.append('openstack.roles.admin')
info.permissions = tuple(info_permissions)

#hide networks from cloud_admin
networks = admin_dashboard.get_panel('networks')
networks_permissions = list(getattr(networks, 'permissions', []))
networks_permissions.append('openstack.roles.admin')
networks.permissions = tuple(networks_permissions)

#hide routers from cloud_admin
routers = admin_dashboard.get_panel('routers')
routers_permissions = list(getattr(routers, 'permissions', []))
routers_permissions.append('openstack.roles.admin')
routers.permissions = tuple(routers_permissions)

#hide volumes from cloud_admin
volumes = admin_dashboard.get_panel('volumes')
volumes_permissions = list(getattr(volumes, 'permissions', []))
volumes_permissions.append('openstack.roles.admin')
volumes.permissions = tuple(volumes_permissions)

#hide identity/domains from "non admins"
identity_dashboard = horizon.get_dashboard('identity')
domains = identity_dashboard.get_panel('domains')
domains_permissions = list(getattr(domains, 'permissions', []))
domains_permissions.append('openstack.roles.admin')
domains.permissions = tuple(domains_permissions)
