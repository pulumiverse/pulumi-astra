# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['StreamingTopicArgs', 'StreamingTopic']

@pulumi.input_type
class StreamingTopicArgs:
    def __init__(__self__, *,
                 cloud_provider: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 region: pulumi.Input[str],
                 tenant_name: pulumi.Input[str],
                 topic: pulumi.Input[str],
                 deletion_protection: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a StreamingTopic resource.
        :param pulumi.Input[str] cloud_provider: Cloud provider
        :param pulumi.Input[str] namespace: Pulsar Namespace
        :param pulumi.Input[str] region: cloud region
        :param pulumi.Input[str] tenant_name: Streaming tenant name.
        :param pulumi.Input[str] topic: Streaming tenant topic.
        :param pulumi.Input[bool] deletion_protection: Whether or not to allow Terraform to destroy this streaming topic. Unless this field is set to false in Terraform state,
               a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
        """
        pulumi.set(__self__, "cloud_provider", cloud_provider)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "tenant_name", tenant_name)
        pulumi.set(__self__, "topic", topic)
        if deletion_protection is not None:
            pulumi.set(__self__, "deletion_protection", deletion_protection)

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> pulumi.Input[str]:
        """
        Cloud provider
        """
        return pulumi.get(self, "cloud_provider")

    @cloud_provider.setter
    def cloud_provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "cloud_provider", value)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        Pulsar Namespace
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        cloud region
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="tenantName")
    def tenant_name(self) -> pulumi.Input[str]:
        """
        Streaming tenant name.
        """
        return pulumi.get(self, "tenant_name")

    @tenant_name.setter
    def tenant_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "tenant_name", value)

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Input[str]:
        """
        Streaming tenant topic.
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: pulumi.Input[str]):
        pulumi.set(self, "topic", value)

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not to allow Terraform to destroy this streaming topic. Unless this field is set to false in Terraform state,
        a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
        """
        return pulumi.get(self, "deletion_protection")

    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deletion_protection", value)


@pulumi.input_type
class _StreamingTopicState:
    def __init__(__self__, *,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_name: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering StreamingTopic resources.
        :param pulumi.Input[str] cloud_provider: Cloud provider
        :param pulumi.Input[bool] deletion_protection: Whether or not to allow Terraform to destroy this streaming topic. Unless this field is set to false in Terraform state,
               a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
        :param pulumi.Input[str] namespace: Pulsar Namespace
        :param pulumi.Input[str] region: cloud region
        :param pulumi.Input[str] tenant_name: Streaming tenant name.
        :param pulumi.Input[str] topic: Streaming tenant topic.
        """
        if cloud_provider is not None:
            pulumi.set(__self__, "cloud_provider", cloud_provider)
        if deletion_protection is not None:
            pulumi.set(__self__, "deletion_protection", deletion_protection)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if tenant_name is not None:
            pulumi.set(__self__, "tenant_name", tenant_name)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> Optional[pulumi.Input[str]]:
        """
        Cloud provider
        """
        return pulumi.get(self, "cloud_provider")

    @cloud_provider.setter
    def cloud_provider(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_provider", value)

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not to allow Terraform to destroy this streaming topic. Unless this field is set to false in Terraform state,
        a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
        """
        return pulumi.get(self, "deletion_protection")

    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deletion_protection", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Pulsar Namespace
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        cloud region
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="tenantName")
    def tenant_name(self) -> Optional[pulumi.Input[str]]:
        """
        Streaming tenant name.
        """
        return pulumi.get(self, "tenant_name")

    @tenant_name.setter
    def tenant_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_name", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        Streaming tenant topic.
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)


class StreamingTopic(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_name: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        `StreamingTopic` creates an Astra Streaming topic.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloud_provider: Cloud provider
        :param pulumi.Input[bool] deletion_protection: Whether or not to allow Terraform to destroy this streaming topic. Unless this field is set to false in Terraform state,
               a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
        :param pulumi.Input[str] namespace: Pulsar Namespace
        :param pulumi.Input[str] region: cloud region
        :param pulumi.Input[str] tenant_name: Streaming tenant name.
        :param pulumi.Input[str] topic: Streaming tenant topic.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StreamingTopicArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `StreamingTopic` creates an Astra Streaming topic.

        :param str resource_name: The name of the resource.
        :param StreamingTopicArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StreamingTopicArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_name: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StreamingTopicArgs.__new__(StreamingTopicArgs)

            if cloud_provider is None and not opts.urn:
                raise TypeError("Missing required property 'cloud_provider'")
            __props__.__dict__["cloud_provider"] = cloud_provider
            __props__.__dict__["deletion_protection"] = deletion_protection
            if namespace is None and not opts.urn:
                raise TypeError("Missing required property 'namespace'")
            __props__.__dict__["namespace"] = namespace
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            if tenant_name is None and not opts.urn:
                raise TypeError("Missing required property 'tenant_name'")
            __props__.__dict__["tenant_name"] = tenant_name
            if topic is None and not opts.urn:
                raise TypeError("Missing required property 'topic'")
            __props__.__dict__["topic"] = topic
        super(StreamingTopic, __self__).__init__(
            'astra:index/streamingTopic:StreamingTopic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cloud_provider: Optional[pulumi.Input[str]] = None,
            deletion_protection: Optional[pulumi.Input[bool]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            tenant_name: Optional[pulumi.Input[str]] = None,
            topic: Optional[pulumi.Input[str]] = None) -> 'StreamingTopic':
        """
        Get an existing StreamingTopic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloud_provider: Cloud provider
        :param pulumi.Input[bool] deletion_protection: Whether or not to allow Terraform to destroy this streaming topic. Unless this field is set to false in Terraform state,
               a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
        :param pulumi.Input[str] namespace: Pulsar Namespace
        :param pulumi.Input[str] region: cloud region
        :param pulumi.Input[str] tenant_name: Streaming tenant name.
        :param pulumi.Input[str] topic: Streaming tenant topic.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StreamingTopicState.__new__(_StreamingTopicState)

        __props__.__dict__["cloud_provider"] = cloud_provider
        __props__.__dict__["deletion_protection"] = deletion_protection
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["region"] = region
        __props__.__dict__["tenant_name"] = tenant_name
        __props__.__dict__["topic"] = topic
        return StreamingTopic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> pulumi.Output[str]:
        """
        Cloud provider
        """
        return pulumi.get(self, "cloud_provider")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not to allow Terraform to destroy this streaming topic. Unless this field is set to false in Terraform state,
        a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
        """
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[str]:
        """
        Pulsar Namespace
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        cloud region
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="tenantName")
    def tenant_name(self) -> pulumi.Output[str]:
        """
        Streaming tenant name.
        """
        return pulumi.get(self, "tenant_name")

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Output[str]:
        """
        Streaming tenant topic.
        """
        return pulumi.get(self, "topic")

