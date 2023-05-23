# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetUsersResult',
    'AwaitableGetUsersResult',
    'get_users',
    'get_users_output',
]

@pulumi.output_type
class GetUsersResult:
    """
    A collection of values returned by getUsers.
    """
    def __init__(__self__, id=None, org_id=None, org_name=None, users=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if org_id and not isinstance(org_id, str):
            raise TypeError("Expected argument 'org_id' to be a str")
        pulumi.set(__self__, "org_id", org_id)
        if org_name and not isinstance(org_name, str):
            raise TypeError("Expected argument 'org_name' to be a str")
        pulumi.set(__self__, "org_name", org_name)
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> str:
        """
        Organization ID.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="orgName")
    def org_name(self) -> Optional[str]:
        """
        Organization Name.
        """
        return pulumi.get(self, "org_name")

    @property
    @pulumi.getter
    def users(self) -> Sequence['outputs.GetUsersUserResult']:
        """
        The list of Astra users.
        """
        return pulumi.get(self, "users")


class AwaitableGetUsersResult(GetUsersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUsersResult(
            id=self.id,
            org_id=self.org_id,
            org_name=self.org_name,
            users=self.users)


def get_users(org_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUsersResult:
    """
    `get_users` provides a datasource for a list of Astra users. This can be used to select users within your Astra Organization.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_astra as astra

    dev = astra.get_users()
    ```


    :param str org_name: Organization Name.
    """
    __args__ = dict()
    __args__['orgName'] = org_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('astra:index/getUsers:getUsers', __args__, opts=opts, typ=GetUsersResult).value

    return AwaitableGetUsersResult(
        id=__ret__.id,
        org_id=__ret__.org_id,
        org_name=__ret__.org_name,
        users=__ret__.users)


@_utilities.lift_output_func(get_users)
def get_users_output(org_name: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUsersResult]:
    """
    `get_users` provides a datasource for a list of Astra users. This can be used to select users within your Astra Organization.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_astra as astra

    dev = astra.get_users()
    ```


    :param str org_name: Organization Name.
    """
    ...