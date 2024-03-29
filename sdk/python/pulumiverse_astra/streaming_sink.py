# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['StreamingSinkArgs', 'StreamingSink']

@pulumi.input_type
class StreamingSinkArgs:
    def __init__(__self__, *,
                 auto_ack: pulumi.Input[bool],
                 cloud_provider: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 parallelism: pulumi.Input[int],
                 processing_guarantees: pulumi.Input[str],
                 region: pulumi.Input[str],
                 retain_ordering: pulumi.Input[bool],
                 sink_configs: pulumi.Input[str],
                 sink_name: pulumi.Input[str],
                 tenant_name: pulumi.Input[str],
                 topic: pulumi.Input[str],
                 deletion_protection: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a StreamingSink resource.
        :param pulumi.Input[bool] auto_ack: auto ack
        :param pulumi.Input[str] cloud_provider: Cloud provider
        :param pulumi.Input[str] namespace: Pulsar Namespace
        :param pulumi.Input[int] parallelism: Parallelism for Pulsar sink
        :param pulumi.Input[str] processing_guarantees: "ATLEAST*ONCE""ATMOST*ONCE""EFFECTIVELY_ONCE".
        :param pulumi.Input[str] region: cloud region
        :param pulumi.Input[bool] retain_ordering: Retain ordering.
        :param pulumi.Input[str] sink_configs: Sink Configs
        :param pulumi.Input[str] sink_name: Name of the sink.
        :param pulumi.Input[str] tenant_name: Streaming tenant name.
        :param pulumi.Input[str] topic: Streaming tenant topic.
        :param pulumi.Input[bool] deletion_protection: Whether or not to allow Terraform to destroy this streaming sink. Unless this field is set to false in Terraform state,
               a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
        """
        pulumi.set(__self__, "auto_ack", auto_ack)
        pulumi.set(__self__, "cloud_provider", cloud_provider)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "parallelism", parallelism)
        pulumi.set(__self__, "processing_guarantees", processing_guarantees)
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "retain_ordering", retain_ordering)
        pulumi.set(__self__, "sink_configs", sink_configs)
        pulumi.set(__self__, "sink_name", sink_name)
        pulumi.set(__self__, "tenant_name", tenant_name)
        pulumi.set(__self__, "topic", topic)
        if deletion_protection is not None:
            pulumi.set(__self__, "deletion_protection", deletion_protection)

    @property
    @pulumi.getter(name="autoAck")
    def auto_ack(self) -> pulumi.Input[bool]:
        """
        auto ack
        """
        return pulumi.get(self, "auto_ack")

    @auto_ack.setter
    def auto_ack(self, value: pulumi.Input[bool]):
        pulumi.set(self, "auto_ack", value)

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
    def parallelism(self) -> pulumi.Input[int]:
        """
        Parallelism for Pulsar sink
        """
        return pulumi.get(self, "parallelism")

    @parallelism.setter
    def parallelism(self, value: pulumi.Input[int]):
        pulumi.set(self, "parallelism", value)

    @property
    @pulumi.getter(name="processingGuarantees")
    def processing_guarantees(self) -> pulumi.Input[str]:
        """
        "ATLEAST*ONCE""ATMOST*ONCE""EFFECTIVELY_ONCE".
        """
        return pulumi.get(self, "processing_guarantees")

    @processing_guarantees.setter
    def processing_guarantees(self, value: pulumi.Input[str]):
        pulumi.set(self, "processing_guarantees", value)

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
    @pulumi.getter(name="retainOrdering")
    def retain_ordering(self) -> pulumi.Input[bool]:
        """
        Retain ordering.
        """
        return pulumi.get(self, "retain_ordering")

    @retain_ordering.setter
    def retain_ordering(self, value: pulumi.Input[bool]):
        pulumi.set(self, "retain_ordering", value)

    @property
    @pulumi.getter(name="sinkConfigs")
    def sink_configs(self) -> pulumi.Input[str]:
        """
        Sink Configs
        """
        return pulumi.get(self, "sink_configs")

    @sink_configs.setter
    def sink_configs(self, value: pulumi.Input[str]):
        pulumi.set(self, "sink_configs", value)

    @property
    @pulumi.getter(name="sinkName")
    def sink_name(self) -> pulumi.Input[str]:
        """
        Name of the sink.
        """
        return pulumi.get(self, "sink_name")

    @sink_name.setter
    def sink_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sink_name", value)

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
        Whether or not to allow Terraform to destroy this streaming sink. Unless this field is set to false in Terraform state,
        a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
        """
        return pulumi.get(self, "deletion_protection")

    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "deletion_protection", value)


@pulumi.input_type
class _StreamingSinkState:
    def __init__(__self__, *,
                 auto_ack: Optional[pulumi.Input[bool]] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 parallelism: Optional[pulumi.Input[int]] = None,
                 processing_guarantees: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 retain_ordering: Optional[pulumi.Input[bool]] = None,
                 sink_configs: Optional[pulumi.Input[str]] = None,
                 sink_name: Optional[pulumi.Input[str]] = None,
                 tenant_name: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering StreamingSink resources.
        :param pulumi.Input[bool] auto_ack: auto ack
        :param pulumi.Input[str] cloud_provider: Cloud provider
        :param pulumi.Input[bool] deletion_protection: Whether or not to allow Terraform to destroy this streaming sink. Unless this field is set to false in Terraform state,
               a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
        :param pulumi.Input[str] namespace: Pulsar Namespace
        :param pulumi.Input[int] parallelism: Parallelism for Pulsar sink
        :param pulumi.Input[str] processing_guarantees: "ATLEAST*ONCE""ATMOST*ONCE""EFFECTIVELY_ONCE".
        :param pulumi.Input[str] region: cloud region
        :param pulumi.Input[bool] retain_ordering: Retain ordering.
        :param pulumi.Input[str] sink_configs: Sink Configs
        :param pulumi.Input[str] sink_name: Name of the sink.
        :param pulumi.Input[str] tenant_name: Streaming tenant name.
        :param pulumi.Input[str] topic: Streaming tenant topic.
        """
        if auto_ack is not None:
            pulumi.set(__self__, "auto_ack", auto_ack)
        if cloud_provider is not None:
            pulumi.set(__self__, "cloud_provider", cloud_provider)
        if deletion_protection is not None:
            pulumi.set(__self__, "deletion_protection", deletion_protection)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if parallelism is not None:
            pulumi.set(__self__, "parallelism", parallelism)
        if processing_guarantees is not None:
            pulumi.set(__self__, "processing_guarantees", processing_guarantees)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if retain_ordering is not None:
            pulumi.set(__self__, "retain_ordering", retain_ordering)
        if sink_configs is not None:
            pulumi.set(__self__, "sink_configs", sink_configs)
        if sink_name is not None:
            pulumi.set(__self__, "sink_name", sink_name)
        if tenant_name is not None:
            pulumi.set(__self__, "tenant_name", tenant_name)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter(name="autoAck")
    def auto_ack(self) -> Optional[pulumi.Input[bool]]:
        """
        auto ack
        """
        return pulumi.get(self, "auto_ack")

    @auto_ack.setter
    def auto_ack(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_ack", value)

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
        Whether or not to allow Terraform to destroy this streaming sink. Unless this field is set to false in Terraform state,
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
    def parallelism(self) -> Optional[pulumi.Input[int]]:
        """
        Parallelism for Pulsar sink
        """
        return pulumi.get(self, "parallelism")

    @parallelism.setter
    def parallelism(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "parallelism", value)

    @property
    @pulumi.getter(name="processingGuarantees")
    def processing_guarantees(self) -> Optional[pulumi.Input[str]]:
        """
        "ATLEAST*ONCE""ATMOST*ONCE""EFFECTIVELY_ONCE".
        """
        return pulumi.get(self, "processing_guarantees")

    @processing_guarantees.setter
    def processing_guarantees(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "processing_guarantees", value)

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
    @pulumi.getter(name="retainOrdering")
    def retain_ordering(self) -> Optional[pulumi.Input[bool]]:
        """
        Retain ordering.
        """
        return pulumi.get(self, "retain_ordering")

    @retain_ordering.setter
    def retain_ordering(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "retain_ordering", value)

    @property
    @pulumi.getter(name="sinkConfigs")
    def sink_configs(self) -> Optional[pulumi.Input[str]]:
        """
        Sink Configs
        """
        return pulumi.get(self, "sink_configs")

    @sink_configs.setter
    def sink_configs(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sink_configs", value)

    @property
    @pulumi.getter(name="sinkName")
    def sink_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the sink.
        """
        return pulumi.get(self, "sink_name")

    @sink_name.setter
    def sink_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sink_name", value)

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


class StreamingSink(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_ack: Optional[pulumi.Input[bool]] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 parallelism: Optional[pulumi.Input[int]] = None,
                 processing_guarantees: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 retain_ordering: Optional[pulumi.Input[bool]] = None,
                 sink_configs: Optional[pulumi.Input[str]] = None,
                 sink_name: Optional[pulumi.Input[str]] = None,
                 tenant_name: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        `StreamingSink` creates a streaming sink which sends data from a topic to a target system.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumiverse_astra as astra

        streaming_tenant_1 = astra.StreamingTenant("streamingTenant-1",
            tenant_name="terraformtest2",
            topic="terraformtest",
            region="useast-4",
            cloud_provider="gcp",
            user_email="seb@datastax.com")
        cdc_1 = astra.Cdc("cdc-1",
            database_id="5b70892f-e01a-4595-98e6-19ecc9985d50",
            database_name="sai_test",
            table="test",
            keyspace="sai_test",
            topic_partitions=3,
            tenant_name=streaming_tenant_1.tenant_name,
            opts=pulumi.ResourceOptions(depends_on=[streaming_tenant_1]))
        streaming_sink_1 = astra.StreamingSink("streamingSink-1",
            tenant_name=streaming_tenant_1.tenant_name,
            topic=cdc_1.data_topic,
            region="useast-4",
            cloud_provider="gcp",
            sink_name="jdbc-clickhouse",
            retain_ordering=True,
            processing_guarantees="ATLEAST_ONCE",
            parallelism=3,
            namespace="default",
            sink_configs=json.dumps({
                "userName": "clickhouse",
                "password": "password",
                "jdbcUrl": "jdbc:clickhouse://fake.clickhouse.url:8123/pulsar_clickhouse_jdbc_sink",
                "tableName": "pulsar_clickhouse_jdbc_sink",
            }),
            auto_ack=True,
            opts=pulumi.ResourceOptions(depends_on=[
                    streaming_tenant_1,
                    cdc_1,
                ]))
        ```

        ## Import

        ```sh
         $ pulumi import astra:index/streamingSink:StreamingSink example tenant_name/topic
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_ack: auto ack
        :param pulumi.Input[str] cloud_provider: Cloud provider
        :param pulumi.Input[bool] deletion_protection: Whether or not to allow Terraform to destroy this streaming sink. Unless this field is set to false in Terraform state,
               a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
        :param pulumi.Input[str] namespace: Pulsar Namespace
        :param pulumi.Input[int] parallelism: Parallelism for Pulsar sink
        :param pulumi.Input[str] processing_guarantees: "ATLEAST*ONCE""ATMOST*ONCE""EFFECTIVELY_ONCE".
        :param pulumi.Input[str] region: cloud region
        :param pulumi.Input[bool] retain_ordering: Retain ordering.
        :param pulumi.Input[str] sink_configs: Sink Configs
        :param pulumi.Input[str] sink_name: Name of the sink.
        :param pulumi.Input[str] tenant_name: Streaming tenant name.
        :param pulumi.Input[str] topic: Streaming tenant topic.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StreamingSinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `StreamingSink` creates a streaming sink which sends data from a topic to a target system.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumiverse_astra as astra

        streaming_tenant_1 = astra.StreamingTenant("streamingTenant-1",
            tenant_name="terraformtest2",
            topic="terraformtest",
            region="useast-4",
            cloud_provider="gcp",
            user_email="seb@datastax.com")
        cdc_1 = astra.Cdc("cdc-1",
            database_id="5b70892f-e01a-4595-98e6-19ecc9985d50",
            database_name="sai_test",
            table="test",
            keyspace="sai_test",
            topic_partitions=3,
            tenant_name=streaming_tenant_1.tenant_name,
            opts=pulumi.ResourceOptions(depends_on=[streaming_tenant_1]))
        streaming_sink_1 = astra.StreamingSink("streamingSink-1",
            tenant_name=streaming_tenant_1.tenant_name,
            topic=cdc_1.data_topic,
            region="useast-4",
            cloud_provider="gcp",
            sink_name="jdbc-clickhouse",
            retain_ordering=True,
            processing_guarantees="ATLEAST_ONCE",
            parallelism=3,
            namespace="default",
            sink_configs=json.dumps({
                "userName": "clickhouse",
                "password": "password",
                "jdbcUrl": "jdbc:clickhouse://fake.clickhouse.url:8123/pulsar_clickhouse_jdbc_sink",
                "tableName": "pulsar_clickhouse_jdbc_sink",
            }),
            auto_ack=True,
            opts=pulumi.ResourceOptions(depends_on=[
                    streaming_tenant_1,
                    cdc_1,
                ]))
        ```

        ## Import

        ```sh
         $ pulumi import astra:index/streamingSink:StreamingSink example tenant_name/topic
        ```

        :param str resource_name: The name of the resource.
        :param StreamingSinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StreamingSinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_ack: Optional[pulumi.Input[bool]] = None,
                 cloud_provider: Optional[pulumi.Input[str]] = None,
                 deletion_protection: Optional[pulumi.Input[bool]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 parallelism: Optional[pulumi.Input[int]] = None,
                 processing_guarantees: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 retain_ordering: Optional[pulumi.Input[bool]] = None,
                 sink_configs: Optional[pulumi.Input[str]] = None,
                 sink_name: Optional[pulumi.Input[str]] = None,
                 tenant_name: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StreamingSinkArgs.__new__(StreamingSinkArgs)

            if auto_ack is None and not opts.urn:
                raise TypeError("Missing required property 'auto_ack'")
            __props__.__dict__["auto_ack"] = auto_ack
            if cloud_provider is None and not opts.urn:
                raise TypeError("Missing required property 'cloud_provider'")
            __props__.__dict__["cloud_provider"] = cloud_provider
            __props__.__dict__["deletion_protection"] = deletion_protection
            if namespace is None and not opts.urn:
                raise TypeError("Missing required property 'namespace'")
            __props__.__dict__["namespace"] = namespace
            if parallelism is None and not opts.urn:
                raise TypeError("Missing required property 'parallelism'")
            __props__.__dict__["parallelism"] = parallelism
            if processing_guarantees is None and not opts.urn:
                raise TypeError("Missing required property 'processing_guarantees'")
            __props__.__dict__["processing_guarantees"] = processing_guarantees
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            if retain_ordering is None and not opts.urn:
                raise TypeError("Missing required property 'retain_ordering'")
            __props__.__dict__["retain_ordering"] = retain_ordering
            if sink_configs is None and not opts.urn:
                raise TypeError("Missing required property 'sink_configs'")
            __props__.__dict__["sink_configs"] = sink_configs
            if sink_name is None and not opts.urn:
                raise TypeError("Missing required property 'sink_name'")
            __props__.__dict__["sink_name"] = sink_name
            if tenant_name is None and not opts.urn:
                raise TypeError("Missing required property 'tenant_name'")
            __props__.__dict__["tenant_name"] = tenant_name
            if topic is None and not opts.urn:
                raise TypeError("Missing required property 'topic'")
            __props__.__dict__["topic"] = topic
        super(StreamingSink, __self__).__init__(
            'astra:index/streamingSink:StreamingSink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_ack: Optional[pulumi.Input[bool]] = None,
            cloud_provider: Optional[pulumi.Input[str]] = None,
            deletion_protection: Optional[pulumi.Input[bool]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            parallelism: Optional[pulumi.Input[int]] = None,
            processing_guarantees: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            retain_ordering: Optional[pulumi.Input[bool]] = None,
            sink_configs: Optional[pulumi.Input[str]] = None,
            sink_name: Optional[pulumi.Input[str]] = None,
            tenant_name: Optional[pulumi.Input[str]] = None,
            topic: Optional[pulumi.Input[str]] = None) -> 'StreamingSink':
        """
        Get an existing StreamingSink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_ack: auto ack
        :param pulumi.Input[str] cloud_provider: Cloud provider
        :param pulumi.Input[bool] deletion_protection: Whether or not to allow Terraform to destroy this streaming sink. Unless this field is set to false in Terraform state,
               a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
        :param pulumi.Input[str] namespace: Pulsar Namespace
        :param pulumi.Input[int] parallelism: Parallelism for Pulsar sink
        :param pulumi.Input[str] processing_guarantees: "ATLEAST*ONCE""ATMOST*ONCE""EFFECTIVELY_ONCE".
        :param pulumi.Input[str] region: cloud region
        :param pulumi.Input[bool] retain_ordering: Retain ordering.
        :param pulumi.Input[str] sink_configs: Sink Configs
        :param pulumi.Input[str] sink_name: Name of the sink.
        :param pulumi.Input[str] tenant_name: Streaming tenant name.
        :param pulumi.Input[str] topic: Streaming tenant topic.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StreamingSinkState.__new__(_StreamingSinkState)

        __props__.__dict__["auto_ack"] = auto_ack
        __props__.__dict__["cloud_provider"] = cloud_provider
        __props__.__dict__["deletion_protection"] = deletion_protection
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["parallelism"] = parallelism
        __props__.__dict__["processing_guarantees"] = processing_guarantees
        __props__.__dict__["region"] = region
        __props__.__dict__["retain_ordering"] = retain_ordering
        __props__.__dict__["sink_configs"] = sink_configs
        __props__.__dict__["sink_name"] = sink_name
        __props__.__dict__["tenant_name"] = tenant_name
        __props__.__dict__["topic"] = topic
        return StreamingSink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoAck")
    def auto_ack(self) -> pulumi.Output[bool]:
        """
        auto ack
        """
        return pulumi.get(self, "auto_ack")

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
        Whether or not to allow Terraform to destroy this streaming sink. Unless this field is set to false in Terraform state,
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
    def parallelism(self) -> pulumi.Output[int]:
        """
        Parallelism for Pulsar sink
        """
        return pulumi.get(self, "parallelism")

    @property
    @pulumi.getter(name="processingGuarantees")
    def processing_guarantees(self) -> pulumi.Output[str]:
        """
        "ATLEAST*ONCE""ATMOST*ONCE""EFFECTIVELY_ONCE".
        """
        return pulumi.get(self, "processing_guarantees")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        cloud region
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="retainOrdering")
    def retain_ordering(self) -> pulumi.Output[bool]:
        """
        Retain ordering.
        """
        return pulumi.get(self, "retain_ordering")

    @property
    @pulumi.getter(name="sinkConfigs")
    def sink_configs(self) -> pulumi.Output[str]:
        """
        Sink Configs
        """
        return pulumi.get(self, "sink_configs")

    @property
    @pulumi.getter(name="sinkName")
    def sink_name(self) -> pulumi.Output[str]:
        """
        Name of the sink.
        """
        return pulumi.get(self, "sink_name")

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

