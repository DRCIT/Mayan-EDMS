from django.utils.translation import ugettext_lazy as _

from mayan.apps.navigation.classes import Link

from .icons import (
    icon_delete_file_delete, icon_download_file_download,
    icon_download_file_list
)
from .permissions import (
    permission_download_file_download, permission_download_file_view
)

link_download_file_delete = Link(
    args='resolved_object.pk', icon_class=icon_delete_file_delete,
    #permissions=(permission_delete_file_delete,),
    tags='dangerous',
    text=_('Delete'), view='storage:download_file_delete'
)
link_download_file_download = Link(
    args='resolved_object.pk', icon_class=icon_download_file_download,
    #permissions=(permission_download_file_download,),
    text=_('Download'),
    view='storage:download_file_download'
)
link_download_file_list = Link(
    icon_class=icon_download_file_list,
    #permissions=(permission_download_file_view,),
    text=_('Download files'),
    view='storage:download_file_list'
)
