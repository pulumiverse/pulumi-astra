# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetAvailableRegionsResult',
    'AwaitableGetAvailableRegionsResult',
    'get_available_regions',
]

@pulumi.output_type
class GetAvailableRegionsResult:
    """
    A collection of values returned by getAvailableRegions.
    """
    def __init__(__self__, id=None, results=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def results(self) -> Sequence['outputs.GetAvailableRegionsResultResult']:
        return pulumi.get(self, "results")


class AwaitableGetAvailableRegionsResult(GetAvailableRegionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAvailableRegionsResult(
            id=self.id,
            results=self.results)


def get_available_regions(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAvailableRegionsResult:
    """
    Retrieve a list of available cloud regions in Astra

    ## Example Usage

    ```python
    import pulumi
    import pulumi_astra as astra

    regions = astra.get_available_regions()
    ```
    """
    __args__ = dict()
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('astra:index/getAvailableRegions:getAvailableRegions', __args__, opts=opts, typ=GetAvailableRegionsResult).value

    return AwaitableGetAvailableRegionsResult(
        id=__ret__.id,
        results=__ret__.results)
