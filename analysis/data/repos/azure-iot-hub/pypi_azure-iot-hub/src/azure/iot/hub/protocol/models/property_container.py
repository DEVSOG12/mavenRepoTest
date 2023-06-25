# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PropertyContainer(Model):
    """The desired and reported properties of the twin. The maximum depth of the
    object is 10.

    :param desired: The collection of desired property key-value pairs. The
     keys are UTF-8 encoded, case-sensitive and up-to 1KB in length. Allowed
     characters exclude UNICODE control characters (segments C0 and C1), '.',
     '$' and space. The desired porperty values are JSON objects, up-to 4KB in
     length.
    :type desired: dict[str, object]
    :param reported: The collection of reported property key-value pairs. The
     keys are UTF-8 encoded, case-sensitive and up-to 1KB in length. Allowed
     characters exclude UNICODE control characters (segments C0 and C1), '.',
     '$' and space. The reported property values are JSON objects, up-to 4KB in
     length.
    :type reported: dict[str, object]
    """

    _attribute_map = {
        "desired": {"key": "desired", "type": "{object}"},
        "reported": {"key": "reported", "type": "{object}"},
    }

    def __init__(self, **kwargs):
        super(PropertyContainer, self).__init__(**kwargs)
        self.desired = kwargs.get("desired", None)
        self.reported = kwargs.get("reported", None)
