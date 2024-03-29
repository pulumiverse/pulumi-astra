# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['PrivateLinkEndpointArgs', 'PrivateLinkEndpoint']

@pulumi.input_type
class PrivateLinkEndpointArgs:
    def __init__(__self__, *,
                 database_id: pulumi.Input[str],
                 datacenter_id: pulumi.Input[str],
                 endpoint_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a PrivateLinkEndpoint resource.
        :param pulumi.Input[str] database_id: The ID of the Astra database.
        :param pulumi.Input[str] datacenter_id: Astra datacenter in the region where the private link will be created.
        :param pulumi.Input[str] endpoint_id: Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
        """
        pulumi.set(__self__, "database_id", database_id)
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "endpoint_id", endpoint_id)

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> pulumi.Input[str]:
        """
        The ID of the Astra database.
        """
        return pulumi.get(self, "database_id")

    @database_id.setter
    def database_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_id", value)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        Astra datacenter in the region where the private link will be created.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> pulumi.Input[str]:
        """
        Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
        """
        return pulumi.get(self, "endpoint_id")

    @endpoint_id.setter
    def endpoint_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_id", value)


@pulumi.input_type
class _PrivateLinkEndpointState:
    def __init__(__self__, *,
                 astra_endpoint_id: Optional[pulumi.Input[str]] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 endpoint_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PrivateLinkEndpoint resources.
        :param pulumi.Input[str] astra_endpoint_id: Endpoint ID for referencing within Astra. May be different than the endpoint_id of this resource.
        :param pulumi.Input[str] database_id: The ID of the Astra database.
        :param pulumi.Input[str] datacenter_id: Astra datacenter in the region where the private link will be created.
        :param pulumi.Input[str] endpoint_id: Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
        """
        if astra_endpoint_id is not None:
            pulumi.set(__self__, "astra_endpoint_id", astra_endpoint_id)
        if database_id is not None:
            pulumi.set(__self__, "database_id", database_id)
        if datacenter_id is not None:
            pulumi.set(__self__, "datacenter_id", datacenter_id)
        if endpoint_id is not None:
            pulumi.set(__self__, "endpoint_id", endpoint_id)

    @property
    @pulumi.getter(name="astraEndpointId")
    def astra_endpoint_id(self) -> Optional[pulumi.Input[str]]:
        """
        Endpoint ID for referencing within Astra. May be different than the endpoint_id of this resource.
        """
        return pulumi.get(self, "astra_endpoint_id")

    @astra_endpoint_id.setter
    def astra_endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "astra_endpoint_id", value)

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Astra database.
        """
        return pulumi.get(self, "database_id")

    @database_id.setter
    def database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_id", value)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> Optional[pulumi.Input[str]]:
        """
        Astra datacenter in the region where the private link will be created.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[pulumi.Input[str]]:
        """
        Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
        """
        return pulumi.get(self, "endpoint_id")

    @endpoint_id.setter
    def endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_id", value)


class PrivateLinkEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 endpoint_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        `PrivateLinkEndpoint` completes the creation of a private link endpoint by associating it with your endpoint.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_azure as azure
        import pulumi_gcp as gcp
        import pulumiverse_astra as astra

        # AWS example
        example_astra_index_private_link_private_link = astra.PrivateLink("exampleAstraIndex/privateLinkPrivateLink",
            allowed_principals=["arn:aws:iam::445559476293:user/Sebastian"],
            database_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588",
            datacenter_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588-1")
        example_vpc_endpoint = aws.ec2.VpcEndpoint("exampleVpcEndpoint",
            vpc_id="vpc-f939e884",
            service_name=example_astra_index / private_link_private_link["serviceName"],
            vpc_endpoint_type="Interface",
            subnet_ids=[
                "subnet-4d376300",
                "subnet-4d85066c",
                "subnet-030e8b65",
            ],
            security_group_ids=["sg-74ae4d41"])
        example_private_link_endpoint = astra.PrivateLinkEndpoint("examplePrivateLinkEndpoint",
            database_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588",
            datacenter_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
            endpoint_id=example_vpc_endpoint.id)
        example_private_link = astra.PrivateLink("examplePrivateLink",
            allowed_principals=["my-project"],
            database_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588",
            datacenter_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588-1")
        example_network = gcp.compute.Network("exampleNetwork", auto_create_subnetworks=False)
        example_subnetwork = gcp.compute.Subnetwork("exampleSubnetwork",
            ip_cidr_range="10.142.0.0/20",
            region="us-east1",
            network=example_network.id)
        example_address = gcp.compute.Address("exampleAddress",
            subnetwork=example_subnetwork.id,
            address_type="INTERNAL",
            region="us-east1")
        example_forwarding_rule = gcp.compute.ForwardingRule("exampleForwardingRule",
            target=f"https://www.googleapis.com/compute/v1/{example_astra_index / private_link_private_link['serviceName']}",
            project=example_network.project,
            ip_address=example_address.id,
            network=example_network.id,
            region="us-east1",
            load_balancing_scheme="")
        # The endpoint ID (PSC Connection ID) is not currently accessible from the google_compute_forwarding_rule terraform object.
        # It must be retrieved via the GCP UI (https://console.cloud.google.com/net-services/psc/list) or via the gcloud CLI:
        #    gcloud compute forwarding-rules describe psc-endpoint --region=us-east1
        endpoint = astra.PrivateLinkEndpoint("endpoint",
            database_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588",
            datacenter_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
            endpoint_id="13585698993864708")
        current = azure.core.get_subscription()
        example_resource_group = azure.core.get_resource_group(name="example-rg")
        example_virtual_network = azure.network.get_virtual_network(name="example-virtual-network",
            resource_group_name=example_resource_group.name)
        example_subnet = azure.network.get_subnet(name="example-subnet",
            virtual_network_name=example_virtual_network.name,
            resource_group_name=example_resource_group.name)
        example_index_private_link_private_link = astra.PrivateLink("exampleIndex/privateLinkPrivateLink",
            allowed_principals=[current.subscription_id],
            database_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588",
            datacenter_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588-1")
        example_endpoint = azure.privatelink.Endpoint("exampleEndpoint",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            subnet_id=example_subnet.id,
            private_service_connection=azure.privatelink.EndpointPrivateServiceConnectionArgs(
                name="example-private-connection",
                private_connection_resource_alias=example_astra_index / private_link_private_link["serviceName"],
                is_manual_connection=True,
                request_message="Private connection from AKS subnet to Astra DB",
            ))
        # NOTE: If you destroy the astra_private_link_endpoint resource for an Azure private endpoint,
        # you will have to destroy and recreate the azurerm_private_endpoint resource in order to
        # reconnect and Astra private link endpoint.
        az_private_link_endpoint = astra.PrivateLinkEndpoint("azPrivateLinkEndpoint",
            database_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588",
            datacenter_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
            endpoint_id=example_endpoint.name.apply(lambda name: f"{example_resource_group.id}/providers/Microsoft.Network/privateEndpoints/{name}"))
        ```

        ## Import

        # Amazon AWS example

        ```sh
         $ pulumi import astra:index/privateLinkEndpoint:PrivateLinkEndpoint example a6bc9c26-e7ce-424f-84c7-0a00afb12588/datacenter/a6bc9c26-e7ce-424f-84c7-0a00afb12588-1/endpoint/vpce-0f7aed6e7a18a1791
        ```

        # Google GCP example

        ```sh
         $ pulumi import astra:index/privateLinkEndpoint:PrivateLinkEndpoint example a6bc9c26-e7ce-424f-84c7-0a00afb12588/datacenter/a6bc9c26-e7ce-424f-84c7-0a00afb12588-1/endpoint/13585698993864708
        ```

        # Azure EKS example

        ```sh
         $ pulumi import astra:index/privateLinkEndpoint:PrivateLinkEndpoint example a6bc9c26-e7ce-424f-84c7-0a00afb12588/datacenter/a6bc9c26-e7ce-424f-84c7-0a00afb12588-1/endpoint/dc5ee5b1-4fc2-463e-a56b-ff54dd38b879/providers/Microsoft.Network/privateEndpoints/private-endpoint-example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_id: The ID of the Astra database.
        :param pulumi.Input[str] datacenter_id: Astra datacenter in the region where the private link will be created.
        :param pulumi.Input[str] endpoint_id: Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateLinkEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `PrivateLinkEndpoint` completes the creation of a private link endpoint by associating it with your endpoint.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_azure as azure
        import pulumi_gcp as gcp
        import pulumiverse_astra as astra

        # AWS example
        example_astra_index_private_link_private_link = astra.PrivateLink("exampleAstraIndex/privateLinkPrivateLink",
            allowed_principals=["arn:aws:iam::445559476293:user/Sebastian"],
            database_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588",
            datacenter_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588-1")
        example_vpc_endpoint = aws.ec2.VpcEndpoint("exampleVpcEndpoint",
            vpc_id="vpc-f939e884",
            service_name=example_astra_index / private_link_private_link["serviceName"],
            vpc_endpoint_type="Interface",
            subnet_ids=[
                "subnet-4d376300",
                "subnet-4d85066c",
                "subnet-030e8b65",
            ],
            security_group_ids=["sg-74ae4d41"])
        example_private_link_endpoint = astra.PrivateLinkEndpoint("examplePrivateLinkEndpoint",
            database_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588",
            datacenter_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
            endpoint_id=example_vpc_endpoint.id)
        example_private_link = astra.PrivateLink("examplePrivateLink",
            allowed_principals=["my-project"],
            database_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588",
            datacenter_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588-1")
        example_network = gcp.compute.Network("exampleNetwork", auto_create_subnetworks=False)
        example_subnetwork = gcp.compute.Subnetwork("exampleSubnetwork",
            ip_cidr_range="10.142.0.0/20",
            region="us-east1",
            network=example_network.id)
        example_address = gcp.compute.Address("exampleAddress",
            subnetwork=example_subnetwork.id,
            address_type="INTERNAL",
            region="us-east1")
        example_forwarding_rule = gcp.compute.ForwardingRule("exampleForwardingRule",
            target=f"https://www.googleapis.com/compute/v1/{example_astra_index / private_link_private_link['serviceName']}",
            project=example_network.project,
            ip_address=example_address.id,
            network=example_network.id,
            region="us-east1",
            load_balancing_scheme="")
        # The endpoint ID (PSC Connection ID) is not currently accessible from the google_compute_forwarding_rule terraform object.
        # It must be retrieved via the GCP UI (https://console.cloud.google.com/net-services/psc/list) or via the gcloud CLI:
        #    gcloud compute forwarding-rules describe psc-endpoint --region=us-east1
        endpoint = astra.PrivateLinkEndpoint("endpoint",
            database_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588",
            datacenter_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
            endpoint_id="13585698993864708")
        current = azure.core.get_subscription()
        example_resource_group = azure.core.get_resource_group(name="example-rg")
        example_virtual_network = azure.network.get_virtual_network(name="example-virtual-network",
            resource_group_name=example_resource_group.name)
        example_subnet = azure.network.get_subnet(name="example-subnet",
            virtual_network_name=example_virtual_network.name,
            resource_group_name=example_resource_group.name)
        example_index_private_link_private_link = astra.PrivateLink("exampleIndex/privateLinkPrivateLink",
            allowed_principals=[current.subscription_id],
            database_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588",
            datacenter_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588-1")
        example_endpoint = azure.privatelink.Endpoint("exampleEndpoint",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            subnet_id=example_subnet.id,
            private_service_connection=azure.privatelink.EndpointPrivateServiceConnectionArgs(
                name="example-private-connection",
                private_connection_resource_alias=example_astra_index / private_link_private_link["serviceName"],
                is_manual_connection=True,
                request_message="Private connection from AKS subnet to Astra DB",
            ))
        # NOTE: If you destroy the astra_private_link_endpoint resource for an Azure private endpoint,
        # you will have to destroy and recreate the azurerm_private_endpoint resource in order to
        # reconnect and Astra private link endpoint.
        az_private_link_endpoint = astra.PrivateLinkEndpoint("azPrivateLinkEndpoint",
            database_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588",
            datacenter_id="a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
            endpoint_id=example_endpoint.name.apply(lambda name: f"{example_resource_group.id}/providers/Microsoft.Network/privateEndpoints/{name}"))
        ```

        ## Import

        # Amazon AWS example

        ```sh
         $ pulumi import astra:index/privateLinkEndpoint:PrivateLinkEndpoint example a6bc9c26-e7ce-424f-84c7-0a00afb12588/datacenter/a6bc9c26-e7ce-424f-84c7-0a00afb12588-1/endpoint/vpce-0f7aed6e7a18a1791
        ```

        # Google GCP example

        ```sh
         $ pulumi import astra:index/privateLinkEndpoint:PrivateLinkEndpoint example a6bc9c26-e7ce-424f-84c7-0a00afb12588/datacenter/a6bc9c26-e7ce-424f-84c7-0a00afb12588-1/endpoint/13585698993864708
        ```

        # Azure EKS example

        ```sh
         $ pulumi import astra:index/privateLinkEndpoint:PrivateLinkEndpoint example a6bc9c26-e7ce-424f-84c7-0a00afb12588/datacenter/a6bc9c26-e7ce-424f-84c7-0a00afb12588-1/endpoint/dc5ee5b1-4fc2-463e-a56b-ff54dd38b879/providers/Microsoft.Network/privateEndpoints/private-endpoint-example
        ```

        :param str resource_name: The name of the resource.
        :param PrivateLinkEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateLinkEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 endpoint_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateLinkEndpointArgs.__new__(PrivateLinkEndpointArgs)

            if database_id is None and not opts.urn:
                raise TypeError("Missing required property 'database_id'")
            __props__.__dict__["database_id"] = database_id
            if datacenter_id is None and not opts.urn:
                raise TypeError("Missing required property 'datacenter_id'")
            __props__.__dict__["datacenter_id"] = datacenter_id
            if endpoint_id is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_id'")
            __props__.__dict__["endpoint_id"] = endpoint_id
            __props__.__dict__["astra_endpoint_id"] = None
        super(PrivateLinkEndpoint, __self__).__init__(
            'astra:index/privateLinkEndpoint:PrivateLinkEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            astra_endpoint_id: Optional[pulumi.Input[str]] = None,
            database_id: Optional[pulumi.Input[str]] = None,
            datacenter_id: Optional[pulumi.Input[str]] = None,
            endpoint_id: Optional[pulumi.Input[str]] = None) -> 'PrivateLinkEndpoint':
        """
        Get an existing PrivateLinkEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] astra_endpoint_id: Endpoint ID for referencing within Astra. May be different than the endpoint_id of this resource.
        :param pulumi.Input[str] database_id: The ID of the Astra database.
        :param pulumi.Input[str] datacenter_id: Astra datacenter in the region where the private link will be created.
        :param pulumi.Input[str] endpoint_id: Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PrivateLinkEndpointState.__new__(_PrivateLinkEndpointState)

        __props__.__dict__["astra_endpoint_id"] = astra_endpoint_id
        __props__.__dict__["database_id"] = database_id
        __props__.__dict__["datacenter_id"] = datacenter_id
        __props__.__dict__["endpoint_id"] = endpoint_id
        return PrivateLinkEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="astraEndpointId")
    def astra_endpoint_id(self) -> pulumi.Output[str]:
        """
        Endpoint ID for referencing within Astra. May be different than the endpoint_id of this resource.
        """
        return pulumi.get(self, "astra_endpoint_id")

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> pulumi.Output[str]:
        """
        The ID of the Astra database.
        """
        return pulumi.get(self, "database_id")

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Output[str]:
        """
        Astra datacenter in the region where the private link will be created.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> pulumi.Output[str]:
        """
        Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
        """
        return pulumi.get(self, "endpoint_id")

