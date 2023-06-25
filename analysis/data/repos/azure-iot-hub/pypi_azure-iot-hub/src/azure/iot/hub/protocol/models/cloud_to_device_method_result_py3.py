# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloudToDeviceMethodResult(Model):
    """Represents the Device Method Invocation Results.

    :param status: Method invocation result status.
    :type status: int
    :param payload: Method invocation result payload.
    :type payload: object
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "payload": {"key": "payload", "type": "object"},
    }

    def __init__(self, *, status: int = None, payload=None, **kwargs) -> None:
        super(CloudToDeviceMethodResult, self).__init__(**kwargs)
        self.status = status
        self.payload = payload
