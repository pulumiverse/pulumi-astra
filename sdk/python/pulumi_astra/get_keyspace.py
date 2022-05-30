# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetKeyspaceResult',
    'AwaitableGetKeyspaceResult',
    'get_keyspace',
    'get_keyspace_output',
]

@pulumi.output_type
class GetKeyspaceResult:
    """
    A collection of values returned by getKeyspace.
    """
    def __init__(__self__, database_id=None, id=None, name=None):
        if database_id and not isinstance(database_id, str):
            raise TypeError("Expected argument 'database_id' to be a str")
        pulumi.set(__self__, "database_id", database_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> str:
        return pulumi.get(self, "database_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetKeyspaceResult(GetKeyspaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeyspaceResult(
            database_id=self.database_id,
            id=self.id,
            name=self.name)


def get_keyspace(database_id: Optional[str] = None,
                 name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeyspaceResult:
    """
    `Keyspace` provides a datasource for a particular keyspace. See `get_keyspaces` if you're looking to fetch all the keyspaces for a particular database.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_astra as astra

    dev = astra.get_keyspace(database_id="f9f4b1e0-4c05-451e-9bba-d631295a7f73",
        name="puppies")
    ```
    """
    __args__ = dict()
    __args__['databaseId'] = database_id
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('astra:index/getKeyspace:getKeyspace', __args__, opts=opts, typ=GetKeyspaceResult).value

    return AwaitableGetKeyspaceResult(
        database_id=__ret__.database_id,
        id=__ret__.id,
        name=__ret__.name)


@_utilities.lift_output_func(get_keyspace)
def get_keyspace_output(database_id: Optional[pulumi.Input[str]] = None,
                        name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKeyspaceResult]:
    """
    `Keyspace` provides a datasource for a particular keyspace. See `get_keyspaces` if you're looking to fetch all the keyspaces for a particular database.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_astra as astra

    dev = astra.get_keyspace(database_id="f9f4b1e0-4c05-451e-9bba-d631295a7f73",
        name="puppies")
    ```
    """
    ...
