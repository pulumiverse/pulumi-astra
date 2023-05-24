# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'AccessListAddressArgs',
]

@pulumi.input_type
class AccessListAddressArgs:
    def __init__(__self__, *,
                 address: pulumi.Input[str],
                 enabled: pulumi.Input[bool],
                 description: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] address: IP Address/CIDR group that should have access
        :param pulumi.Input[bool] enabled: Enable/disable this IP Address/CIDR group's access
        :param pulumi.Input[str] description: Description for the IP Address/CIDR group
        """
        pulumi.set(__self__, "address", address)
        pulumi.set(__self__, "enabled", enabled)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Input[str]:
        """
        IP Address/CIDR group that should have access
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: pulumi.Input[str]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Enable/disable this IP Address/CIDR group's access
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description for the IP Address/CIDR group
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


