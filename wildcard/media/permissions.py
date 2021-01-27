from AccessControl.Permission import addPermission
from AccessControl.SecurityInfo import ModuleSecurityInfo

# http://developer.plone.org/security/custom_permissions.html
security = ModuleSecurityInfo('plone.app.contenttypes')
TYPE_ROLES = ('Manager', 'Site Administrator', 'Owner', 'Contributor')

security.declarePublic('wildcard.media.AddWildcardVideo')
addPermission('wildcard.media.AddWildcardVideo', TYPE_ROLES)
AddWildcardVideo = "wildcard.media.AddWildcardVideo"

security.declarePublic('wildcard.media.AddWildcardAudio')
addPermission('wildcard.media.AddWildcardAudio', TYPE_ROLES)
AddWildcardAudio = "wildcard.media.AddWildcardAudio"
