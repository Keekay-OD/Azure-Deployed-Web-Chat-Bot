# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AttachmentView(Model):
    """Attachment View name and size.

    :param view_id: Content type of the attachment
    :type view_id: str
    :param size: Name of the attachment
    :type size: int
    """

    _attribute_map = {
        'view_id': {'key': 'viewId', 'type': 'str'},
        'size': {'key': 'size', 'type': 'int'},
    }

    def __init__(self, *, view_id: str=None, size: int=None, **kwargs) -> None:
        super(AttachmentView, self).__init__(**kwargs)
        self.view_id = view_id
        self.size = size
