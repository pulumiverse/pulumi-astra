# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CdcArgs', 'Cdc']

@pulumi.input_type
class CdcArgs:
    def __init__(__self__, *,
                 database_id: pulumi.Input[str],
                 database_name: pulumi.Input[str],
                 keyspace: pulumi.Input[str],
                 table: pulumi.Input[str],
                 tenant_name: pulumi.Input[str],
                 topic_partitions: pulumi.Input[int]):
        """
        The set of arguments for constructing a Cdc resource.
        :param pulumi.Input[str] database_id: Astra database to create the keyspace.
        :param pulumi.Input[str] database_name: Astra database name.
        :param pulumi.Input[str] keyspace: Initial keyspace name. For additional keyspaces, use the astra_keyspace resource.
        :param pulumi.Input[str] table: Astra database table.
        :param pulumi.Input[str] tenant_name: Streaming tenant name
        :param pulumi.Input[int] topic_partitions: Number of partitions in cdc topic.
        """
        pulumi.set(__self__, "database_id", database_id)
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "keyspace", keyspace)
        pulumi.set(__self__, "table", table)
        pulumi.set(__self__, "tenant_name", tenant_name)
        pulumi.set(__self__, "topic_partitions", topic_partitions)

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> pulumi.Input[str]:
        """
        Astra database to create the keyspace.
        """
        return pulumi.get(self, "database_id")

    @database_id.setter
    def database_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_id", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        Astra database name.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def keyspace(self) -> pulumi.Input[str]:
        """
        Initial keyspace name. For additional keyspaces, use the astra_keyspace resource.
        """
        return pulumi.get(self, "keyspace")

    @keyspace.setter
    def keyspace(self, value: pulumi.Input[str]):
        pulumi.set(self, "keyspace", value)

    @property
    @pulumi.getter
    def table(self) -> pulumi.Input[str]:
        """
        Astra database table.
        """
        return pulumi.get(self, "table")

    @table.setter
    def table(self, value: pulumi.Input[str]):
        pulumi.set(self, "table", value)

    @property
    @pulumi.getter(name="tenantName")
    def tenant_name(self) -> pulumi.Input[str]:
        """
        Streaming tenant name
        """
        return pulumi.get(self, "tenant_name")

    @tenant_name.setter
    def tenant_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "tenant_name", value)

    @property
    @pulumi.getter(name="topicPartitions")
    def topic_partitions(self) -> pulumi.Input[int]:
        """
        Number of partitions in cdc topic.
        """
        return pulumi.get(self, "topic_partitions")

    @topic_partitions.setter
    def topic_partitions(self, value: pulumi.Input[int]):
        pulumi.set(self, "topic_partitions", value)


@pulumi.input_type
class _CdcState:
    def __init__(__self__, *,
                 connector_status: Optional[pulumi.Input[str]] = None,
                 data_topic: Optional[pulumi.Input[str]] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 keyspace: Optional[pulumi.Input[str]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 tenant_name: Optional[pulumi.Input[str]] = None,
                 topic_partitions: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Cdc resources.
        :param pulumi.Input[str] connector_status: Streaming tenant name
        :param pulumi.Input[str] data_topic: Streaming tenant name
        :param pulumi.Input[str] database_id: Astra database to create the keyspace.
        :param pulumi.Input[str] database_name: Astra database name.
        :param pulumi.Input[str] keyspace: Initial keyspace name. For additional keyspaces, use the astra_keyspace resource.
        :param pulumi.Input[str] table: Astra database table.
        :param pulumi.Input[str] tenant_name: Streaming tenant name
        :param pulumi.Input[int] topic_partitions: Number of partitions in cdc topic.
        """
        if connector_status is not None:
            pulumi.set(__self__, "connector_status", connector_status)
        if data_topic is not None:
            pulumi.set(__self__, "data_topic", data_topic)
        if database_id is not None:
            pulumi.set(__self__, "database_id", database_id)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if keyspace is not None:
            pulumi.set(__self__, "keyspace", keyspace)
        if table is not None:
            pulumi.set(__self__, "table", table)
        if tenant_name is not None:
            pulumi.set(__self__, "tenant_name", tenant_name)
        if topic_partitions is not None:
            pulumi.set(__self__, "topic_partitions", topic_partitions)

    @property
    @pulumi.getter(name="connectorStatus")
    def connector_status(self) -> Optional[pulumi.Input[str]]:
        """
        Streaming tenant name
        """
        return pulumi.get(self, "connector_status")

    @connector_status.setter
    def connector_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_status", value)

    @property
    @pulumi.getter(name="dataTopic")
    def data_topic(self) -> Optional[pulumi.Input[str]]:
        """
        Streaming tenant name
        """
        return pulumi.get(self, "data_topic")

    @data_topic.setter
    def data_topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_topic", value)

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> Optional[pulumi.Input[str]]:
        """
        Astra database to create the keyspace.
        """
        return pulumi.get(self, "database_id")

    @database_id.setter
    def database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_id", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        Astra database name.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def keyspace(self) -> Optional[pulumi.Input[str]]:
        """
        Initial keyspace name. For additional keyspaces, use the astra_keyspace resource.
        """
        return pulumi.get(self, "keyspace")

    @keyspace.setter
    def keyspace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "keyspace", value)

    @property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[str]]:
        """
        Astra database table.
        """
        return pulumi.get(self, "table")

    @table.setter
    def table(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table", value)

    @property
    @pulumi.getter(name="tenantName")
    def tenant_name(self) -> Optional[pulumi.Input[str]]:
        """
        Streaming tenant name
        """
        return pulumi.get(self, "tenant_name")

    @tenant_name.setter
    def tenant_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_name", value)

    @property
    @pulumi.getter(name="topicPartitions")
    def topic_partitions(self) -> Optional[pulumi.Input[int]]:
        """
        Number of partitions in cdc topic.
        """
        return pulumi.get(self, "topic_partitions")

    @topic_partitions.setter
    def topic_partitions(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "topic_partitions", value)


class Cdc(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 keyspace: Optional[pulumi.Input[str]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 tenant_name: Optional[pulumi.Input[str]] = None,
                 topic_partitions: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        `Cdc` enables cdc for an Astra Serverless table.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_astra as astra

        streaming_tenant_1 = astra.StreamingTenant("streamingTenant-1",
            tenant_name="terraformtest",
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
        ```

        ## Import

        ```sh
         $ pulumi import astra:index/cdc:Cdc example databaseId/keyspace/table/tenantName
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_id: Astra database to create the keyspace.
        :param pulumi.Input[str] database_name: Astra database name.
        :param pulumi.Input[str] keyspace: Initial keyspace name. For additional keyspaces, use the astra_keyspace resource.
        :param pulumi.Input[str] table: Astra database table.
        :param pulumi.Input[str] tenant_name: Streaming tenant name
        :param pulumi.Input[int] topic_partitions: Number of partitions in cdc topic.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CdcArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `Cdc` enables cdc for an Astra Serverless table.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_astra as astra

        streaming_tenant_1 = astra.StreamingTenant("streamingTenant-1",
            tenant_name="terraformtest",
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
        ```

        ## Import

        ```sh
         $ pulumi import astra:index/cdc:Cdc example databaseId/keyspace/table/tenantName
        ```

        :param str resource_name: The name of the resource.
        :param CdcArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CdcArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 keyspace: Optional[pulumi.Input[str]] = None,
                 table: Optional[pulumi.Input[str]] = None,
                 tenant_name: Optional[pulumi.Input[str]] = None,
                 topic_partitions: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CdcArgs.__new__(CdcArgs)

            if database_id is None and not opts.urn:
                raise TypeError("Missing required property 'database_id'")
            __props__.__dict__["database_id"] = database_id
            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            if keyspace is None and not opts.urn:
                raise TypeError("Missing required property 'keyspace'")
            __props__.__dict__["keyspace"] = keyspace
            if table is None and not opts.urn:
                raise TypeError("Missing required property 'table'")
            __props__.__dict__["table"] = table
            if tenant_name is None and not opts.urn:
                raise TypeError("Missing required property 'tenant_name'")
            __props__.__dict__["tenant_name"] = tenant_name
            if topic_partitions is None and not opts.urn:
                raise TypeError("Missing required property 'topic_partitions'")
            __props__.__dict__["topic_partitions"] = topic_partitions
            __props__.__dict__["connector_status"] = None
            __props__.__dict__["data_topic"] = None
        super(Cdc, __self__).__init__(
            'astra:index/cdc:Cdc',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connector_status: Optional[pulumi.Input[str]] = None,
            data_topic: Optional[pulumi.Input[str]] = None,
            database_id: Optional[pulumi.Input[str]] = None,
            database_name: Optional[pulumi.Input[str]] = None,
            keyspace: Optional[pulumi.Input[str]] = None,
            table: Optional[pulumi.Input[str]] = None,
            tenant_name: Optional[pulumi.Input[str]] = None,
            topic_partitions: Optional[pulumi.Input[int]] = None) -> 'Cdc':
        """
        Get an existing Cdc resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connector_status: Streaming tenant name
        :param pulumi.Input[str] data_topic: Streaming tenant name
        :param pulumi.Input[str] database_id: Astra database to create the keyspace.
        :param pulumi.Input[str] database_name: Astra database name.
        :param pulumi.Input[str] keyspace: Initial keyspace name. For additional keyspaces, use the astra_keyspace resource.
        :param pulumi.Input[str] table: Astra database table.
        :param pulumi.Input[str] tenant_name: Streaming tenant name
        :param pulumi.Input[int] topic_partitions: Number of partitions in cdc topic.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CdcState.__new__(_CdcState)

        __props__.__dict__["connector_status"] = connector_status
        __props__.__dict__["data_topic"] = data_topic
        __props__.__dict__["database_id"] = database_id
        __props__.__dict__["database_name"] = database_name
        __props__.__dict__["keyspace"] = keyspace
        __props__.__dict__["table"] = table
        __props__.__dict__["tenant_name"] = tenant_name
        __props__.__dict__["topic_partitions"] = topic_partitions
        return Cdc(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectorStatus")
    def connector_status(self) -> pulumi.Output[str]:
        """
        Streaming tenant name
        """
        return pulumi.get(self, "connector_status")

    @property
    @pulumi.getter(name="dataTopic")
    def data_topic(self) -> pulumi.Output[str]:
        """
        Streaming tenant name
        """
        return pulumi.get(self, "data_topic")

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> pulumi.Output[str]:
        """
        Astra database to create the keyspace.
        """
        return pulumi.get(self, "database_id")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[str]:
        """
        Astra database name.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def keyspace(self) -> pulumi.Output[str]:
        """
        Initial keyspace name. For additional keyspaces, use the astra_keyspace resource.
        """
        return pulumi.get(self, "keyspace")

    @property
    @pulumi.getter
    def table(self) -> pulumi.Output[str]:
        """
        Astra database table.
        """
        return pulumi.get(self, "table")

    @property
    @pulumi.getter(name="tenantName")
    def tenant_name(self) -> pulumi.Output[str]:
        """
        Streaming tenant name
        """
        return pulumi.get(self, "tenant_name")

    @property
    @pulumi.getter(name="topicPartitions")
    def topic_partitions(self) -> pulumi.Output[int]:
        """
        Number of partitions in cdc topic.
        """
        return pulumi.get(self, "topic_partitions")

