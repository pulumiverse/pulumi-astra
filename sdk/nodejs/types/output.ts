// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface AccessListAddress {
    /**
     * IP Address/CIDR group that should have access
     */
    address: string;
    /**
     * Description for the IP Address/CIDR group
     */
    description?: string;
    /**
     * Enable/disable this IP Address/CIDR group's access
     */
    enabled: boolean;
}

export interface GetAccessListAddress {
    address: string;
    description?: string;
    /**
     * The Access list is enabled or disabled.
     */
    enabled: boolean;
}

export interface GetAstraDatabasesResult {
    additionalKeyspaces: string[];
    /**
     * The cloud provider
     */
    cloudProvider: string;
    cqlshUrl: string;
    dataEndpointUrl: string;
    datacenters: {[key: string]: string};
    grafanaUrl: string;
    graphqlUrl: string;
    /**
     * The ID of this resource.
     */
    id: string;
    keyspace: string;
    name: string;
    nodeCount: number;
    organizationId: string;
    ownerId: string;
    regions: string[];
    replicationFactor: number;
    /**
     * Status flter. Only return databases with matching status, if supplied. Otherwise return all databases matching other requirements
     */
    status: string;
    totalStorage: number;
}

export interface GetAvailableRegionsResult {
    cloudProvider: string;
    displayName: string;
    region: string;
    zone: string;
}

export interface GetKeyspacesResult {
    name: string;
}

export interface GetPrivateLinkEndpointsResult {
    createTime: string;
    description: string;
    /**
     * Endpoint ID.
     */
    endpointId: string;
    status: string;
}

export interface GetPrivateLinksResult {
    allowedPrincipals: string[];
    /**
     * The datacenter where of the Astra database.
     */
    datacenterId: string;
    endpoints: string[];
    serviceName: string;
}

export interface GetRolesResult {
    description: string;
    effect: string;
    policies: string[];
    resources: string[];
    roleId: string;
    roleName: string;
}

export interface GetSecureConnectBundleUrlSecureBundle {
    customDomainBundles: outputs.GetSecureConnectBundleUrlSecureBundleCustomDomainBundle[];
    /**
     * The ID of the Astra datacenter. If omitted, all bundles will be fetched.
     */
    datacenterId: string;
    internalMigrationProxyUrl: string;
    internalUrl: string;
    migrationProxyUrl: string;
    url: string;
}

export interface GetSecureConnectBundleUrlSecureBundleCustomDomainBundle {
    apiFqdn: string;
    cqlFqdn: string;
    dashboardFqdn: string;
    domain: string;
    url: string;
}

export interface GetStreamingTenantTokensToken {
    iat: number;
    iss: string;
    sub: string;
    token: string;
    tokenId: string;
}

export interface GetUsersUser {
    email: string;
    roles: outputs.GetUsersUserRole[];
    status: string;
    userId: string;
}

export interface GetUsersUserRole {
    roleId: string;
}

