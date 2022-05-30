# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['RoleArgs', 'Role']

@pulumi.input_type
class RoleArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 effect: pulumi.Input[str],
                 policies: pulumi.Input[Sequence[pulumi.Input[str]]],
                 resources: pulumi.Input[Sequence[pulumi.Input[str]]],
                 role_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a Role resource.
        :param pulumi.Input[str] description: Role description
        :param pulumi.Input[str] effect: Role effect
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: List of policies for the role. See
               https://docs.datastax.com/en/astra/docs/user-permissions.html#_operational_roles_detail for supported policies.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resources: Resources for which role is applicable (format is "drn:astra:org:<org UUID>", followed by optional resource criteria.
               See example usage above).
        :param pulumi.Input[str] role_name: Role name
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "effect", effect)
        pulumi.set(__self__, "policies", policies)
        pulumi.set(__self__, "resources", resources)
        pulumi.set(__self__, "role_name", role_name)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        Role description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def effect(self) -> pulumi.Input[str]:
        """
        Role effect
        """
        return pulumi.get(self, "effect")

    @effect.setter
    def effect(self, value: pulumi.Input[str]):
        pulumi.set(self, "effect", value)

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of policies for the role. See
        https://docs.datastax.com/en/astra/docs/user-permissions.html#_operational_roles_detail for supported policies.
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Resources for which role is applicable (format is "drn:astra:org:<org UUID>", followed by optional resource criteria.
        See example usage above).
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Input[str]:
        """
        Role name
        """
        return pulumi.get(self, "role_name")

    @role_name.setter
    def role_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_name", value)


@pulumi.input_type
class _RoleState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 effect: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role_id: Optional[pulumi.Input[str]] = None,
                 role_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Role resources.
        :param pulumi.Input[str] description: Role description
        :param pulumi.Input[str] effect: Role effect
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: List of policies for the role. See
               https://docs.datastax.com/en/astra/docs/user-permissions.html#_operational_roles_detail for supported policies.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resources: Resources for which role is applicable (format is "drn:astra:org:<org UUID>", followed by optional resource criteria.
               See example usage above).
        :param pulumi.Input[str] role_id: Role ID, system generated
        :param pulumi.Input[str] role_name: Role name
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if effect is not None:
            pulumi.set(__self__, "effect", effect)
        if policies is not None:
            pulumi.set(__self__, "policies", policies)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)
        if role_id is not None:
            pulumi.set(__self__, "role_id", role_id)
        if role_name is not None:
            pulumi.set(__self__, "role_name", role_name)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Role description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[str]]:
        """
        Role effect
        """
        return pulumi.get(self, "effect")

    @effect.setter
    def effect(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "effect", value)

    @property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of policies for the role. See
        https://docs.datastax.com/en/astra/docs/user-permissions.html#_operational_roles_detail for supported policies.
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Resources for which role is applicable (format is "drn:astra:org:<org UUID>", followed by optional resource criteria.
        See example usage above).
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> Optional[pulumi.Input[str]]:
        """
        Role ID, system generated
        """
        return pulumi.get(self, "role_id")

    @role_id.setter
    def role_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_id", value)

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[str]]:
        """
        Role name
        """
        return pulumi.get(self, "role_name")

    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_name", value)


class Role(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 effect: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        `Role` resource represents custom roles for a particular Astra Org. Custom roles can be assigned to an Astra user is to grant them granular permissions when the default roles in the UI are not specific enough. Roles are composed of policies which are granted to resources.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_astra as astra

        example = astra.Role("example",
            description="test role",
            effect="allow",
            policies=["db-all-keyspace-create"],
            resources=["drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73"],
            role_name="puppies")
        example2 = astra.Role("example2",
            description="complex role",
            effect="allow",
            policies=[
                "accesslist-read",
                "db-all-keyspace-describe",
                "db-keyspace-describe",
                "db-table-select",
                "db-table-describe",
                "db-graphql",
                "db-rest",
                "db-cql",
            ],
            resources=[
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73",
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73:db:5b70892f-e01a-4595-98e6-19ecc9985d50",
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73:db:5b70892f-e01a-4595-98e6-19ecc9985d50:keyspace:system_schema:table:*",
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73:db:5b70892f-e01a-4595-98e6-19ecc9985d50:keyspace:system:table:*",
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73:db:5b70892f-e01a-4595-98e6-19ecc9985d50:keyspace:system_virtual_schema:table:*",
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73:db:5b70892f-e01a-4595-98e6-19ecc9985d50:keyspace:*",
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73:db:5b70892f-e01a-4595-98e6-19ecc9985d50:keyspace:*:table:*",
            ],
            role_name="puppies")
        ```

        ## Import

        ```sh
         $ pulumi import astra:index/role:Role example role-id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Role description
        :param pulumi.Input[str] effect: Role effect
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: List of policies for the role. See
               https://docs.datastax.com/en/astra/docs/user-permissions.html#_operational_roles_detail for supported policies.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resources: Resources for which role is applicable (format is "drn:astra:org:<org UUID>", followed by optional resource criteria.
               See example usage above).
        :param pulumi.Input[str] role_name: Role name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `Role` resource represents custom roles for a particular Astra Org. Custom roles can be assigned to an Astra user is to grant them granular permissions when the default roles in the UI are not specific enough. Roles are composed of policies which are granted to resources.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_astra as astra

        example = astra.Role("example",
            description="test role",
            effect="allow",
            policies=["db-all-keyspace-create"],
            resources=["drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73"],
            role_name="puppies")
        example2 = astra.Role("example2",
            description="complex role",
            effect="allow",
            policies=[
                "accesslist-read",
                "db-all-keyspace-describe",
                "db-keyspace-describe",
                "db-table-select",
                "db-table-describe",
                "db-graphql",
                "db-rest",
                "db-cql",
            ],
            resources=[
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73",
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73:db:5b70892f-e01a-4595-98e6-19ecc9985d50",
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73:db:5b70892f-e01a-4595-98e6-19ecc9985d50:keyspace:system_schema:table:*",
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73:db:5b70892f-e01a-4595-98e6-19ecc9985d50:keyspace:system:table:*",
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73:db:5b70892f-e01a-4595-98e6-19ecc9985d50:keyspace:system_virtual_schema:table:*",
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73:db:5b70892f-e01a-4595-98e6-19ecc9985d50:keyspace:*",
                "drn:astra:org:f9f4b1e0-4c05-451e-9bba-d631295a7f73:db:5b70892f-e01a-4595-98e6-19ecc9985d50:keyspace:*:table:*",
            ],
            role_name="puppies")
        ```

        ## Import

        ```sh
         $ pulumi import astra:index/role:Role example role-id
        ```

        :param str resource_name: The name of the resource.
        :param RoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 effect: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = RoleArgs.__new__(RoleArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if effect is None and not opts.urn:
                raise TypeError("Missing required property 'effect'")
            __props__.__dict__["effect"] = effect
            if policies is None and not opts.urn:
                raise TypeError("Missing required property 'policies'")
            __props__.__dict__["policies"] = policies
            if resources is None and not opts.urn:
                raise TypeError("Missing required property 'resources'")
            __props__.__dict__["resources"] = resources
            if role_name is None and not opts.urn:
                raise TypeError("Missing required property 'role_name'")
            __props__.__dict__["role_name"] = role_name
            __props__.__dict__["role_id"] = None
        super(Role, __self__).__init__(
            'astra:index/role:Role',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            effect: Optional[pulumi.Input[str]] = None,
            policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            role_id: Optional[pulumi.Input[str]] = None,
            role_name: Optional[pulumi.Input[str]] = None) -> 'Role':
        """
        Get an existing Role resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Role description
        :param pulumi.Input[str] effect: Role effect
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: List of policies for the role. See
               https://docs.datastax.com/en/astra/docs/user-permissions.html#_operational_roles_detail for supported policies.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resources: Resources for which role is applicable (format is "drn:astra:org:<org UUID>", followed by optional resource criteria.
               See example usage above).
        :param pulumi.Input[str] role_id: Role ID, system generated
        :param pulumi.Input[str] role_name: Role name
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RoleState.__new__(_RoleState)

        __props__.__dict__["description"] = description
        __props__.__dict__["effect"] = effect
        __props__.__dict__["policies"] = policies
        __props__.__dict__["resources"] = resources
        __props__.__dict__["role_id"] = role_id
        __props__.__dict__["role_name"] = role_name
        return Role(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Role description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def effect(self) -> pulumi.Output[str]:
        """
        Role effect
        """
        return pulumi.get(self, "effect")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Sequence[str]]:
        """
        List of policies for the role. See
        https://docs.datastax.com/en/astra/docs/user-permissions.html#_operational_roles_detail for supported policies.
        """
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence[str]]:
        """
        Resources for which role is applicable (format is "drn:astra:org:<org UUID>", followed by optional resource criteria.
        See example usage above).
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> pulumi.Output[str]:
        """
        Role ID, system generated
        """
        return pulumi.get(self, "role_id")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Output[str]:
        """
        Role name
        """
        return pulumi.get(self, "role_name")

