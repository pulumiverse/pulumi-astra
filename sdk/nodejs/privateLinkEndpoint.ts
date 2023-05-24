// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * `astra.PrivateLinkEndpoint` completes the creation of a private link endpoint by associating it with your endpoint.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as astra from "@pulumiverse/astra";
 * import * as aws from "@pulumi/aws";
 * import * as azure from "@pulumi/azure";
 * import * as gcp from "@pulumi/gcp";
 *
 * // AWS example
 * const exampleAstraIndex_privateLinkPrivateLink = new astra.PrivateLink("exampleAstraIndex/privateLinkPrivateLink", {
 *     allowedPrincipals: ["arn:aws:iam::445559476293:user/Sebastian"],
 *     databaseId: "a6bc9c26-e7ce-424f-84c7-0a00afb12588",
 *     datacenterId: "a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
 * });
 * const exampleVpcEndpoint = new aws.ec2.VpcEndpoint("exampleVpcEndpoint", {
 *     vpcId: "vpc-f939e884",
 *     serviceName: exampleAstraIndex / privateLinkPrivateLink.serviceName,
 *     vpcEndpointType: "Interface",
 *     subnetIds: [
 *         "subnet-4d376300",
 *         "subnet-4d85066c",
 *         "subnet-030e8b65",
 *     ],
 *     securityGroupIds: ["sg-74ae4d41"],
 * });
 * const examplePrivateLinkEndpoint = new astra.PrivateLinkEndpoint("examplePrivateLinkEndpoint", {
 *     databaseId: "a6bc9c26-e7ce-424f-84c7-0a00afb12588",
 *     datacenterId: "a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
 *     endpointId: exampleVpcEndpoint.id,
 * });
 * const examplePrivateLink = new astra.PrivateLink("examplePrivateLink", {
 *     allowedPrincipals: ["my-project"],
 *     databaseId: "a6bc9c26-e7ce-424f-84c7-0a00afb12588",
 *     datacenterId: "a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
 * });
 * const exampleNetwork = new gcp.compute.Network("exampleNetwork", {autoCreateSubnetworks: false});
 * const exampleSubnetwork = new gcp.compute.Subnetwork("exampleSubnetwork", {
 *     ipCidrRange: "10.142.0.0/20",
 *     region: "us-east1",
 *     network: exampleNetwork.id,
 * });
 * const exampleAddress = new gcp.compute.Address("exampleAddress", {
 *     subnetwork: exampleSubnetwork.id,
 *     addressType: "INTERNAL",
 *     region: "us-east1",
 * });
 * const exampleForwardingRule = new gcp.compute.ForwardingRule("exampleForwardingRule", {
 *     target: `https://www.googleapis.com/compute/v1/${exampleAstraIndex / privateLinkPrivateLink.serviceName}`,
 *     project: exampleNetwork.project,
 *     ipAddress: exampleAddress.id,
 *     network: exampleNetwork.id,
 *     region: "us-east1",
 *     loadBalancingScheme: "",
 * });
 * // The endpoint ID (PSC Connection ID) is not currently accessible from the google_compute_forwarding_rule terraform object.
 * // It must be retrieved via the GCP UI (https://console.cloud.google.com/net-services/psc/list) or via the gcloud CLI:
 * //    gcloud compute forwarding-rules describe psc-endpoint --region=us-east1
 * const endpoint = new astra.PrivateLinkEndpoint("endpoint", {
 *     databaseId: "a6bc9c26-e7ce-424f-84c7-0a00afb12588",
 *     datacenterId: "a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
 *     endpointId: "13585698993864708",
 * });
 * const current = azure.core.getSubscription({});
 * const exampleResourceGroup = azure.core.getResourceGroup({
 *     name: "example-rg",
 * });
 * const exampleVirtualNetwork = exampleResourceGroup.then(exampleResourceGroup => azure.network.getVirtualNetwork({
 *     name: "example-virtual-network",
 *     resourceGroupName: exampleResourceGroup.name,
 * }));
 * const exampleSubnet = Promise.all([exampleVirtualNetwork, exampleResourceGroup]).then(([exampleVirtualNetwork, exampleResourceGroup]) => azure.network.getSubnet({
 *     name: "example-subnet",
 *     virtualNetworkName: exampleVirtualNetwork.name,
 *     resourceGroupName: exampleResourceGroup.name,
 * }));
 * const exampleIndex_privateLinkPrivateLink = new astra.PrivateLink("exampleIndex/privateLinkPrivateLink", {
 *     allowedPrincipals: [current.then(current => current.subscriptionId)],
 *     databaseId: "a6bc9c26-e7ce-424f-84c7-0a00afb12588",
 *     datacenterId: "a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
 * });
 * const exampleEndpoint = new azure.privatelink.Endpoint("exampleEndpoint", {
 *     location: exampleResourceGroup.then(exampleResourceGroup => exampleResourceGroup.location),
 *     resourceGroupName: exampleResourceGroup.then(exampleResourceGroup => exampleResourceGroup.name),
 *     subnetId: exampleSubnet.then(exampleSubnet => exampleSubnet.id),
 *     privateServiceConnection: {
 *         name: "example-private-connection",
 *         privateConnectionResourceAlias: exampleAstraIndex / privateLinkPrivateLink.serviceName,
 *         isManualConnection: true,
 *         requestMessage: "Private connection from AKS subnet to Astra DB",
 *     },
 * });
 * // NOTE: If you destroy the astra_private_link_endpoint resource for an Azure private endpoint,
 * // you will have to destroy and recreate the azurerm_private_endpoint resource in order to
 * // reconnect and Astra private link endpoint.
 * const azPrivateLinkEndpoint = new astra.PrivateLinkEndpoint("azPrivateLinkEndpoint", {
 *     databaseId: "a6bc9c26-e7ce-424f-84c7-0a00afb12588",
 *     datacenterId: "a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
 *     endpointId: pulumi.all([exampleResourceGroup, exampleEndpoint.name]).apply(([exampleResourceGroup, name]) => `${exampleResourceGroup.id}/providers/Microsoft.Network/privateEndpoints/${name}`),
 * });
 * ```
 *
 * ## Import
 *
 * # Amazon AWS example
 *
 * ```sh
 *  $ pulumi import astra:index/privateLinkEndpoint:PrivateLinkEndpoint example a6bc9c26-e7ce-424f-84c7-0a00afb12588/datacenter/a6bc9c26-e7ce-424f-84c7-0a00afb12588-1/endpoint/vpce-0f7aed6e7a18a1791
 * ```
 *
 * # Google GCP example
 *
 * ```sh
 *  $ pulumi import astra:index/privateLinkEndpoint:PrivateLinkEndpoint example a6bc9c26-e7ce-424f-84c7-0a00afb12588/datacenter/a6bc9c26-e7ce-424f-84c7-0a00afb12588-1/endpoint/13585698993864708
 * ```
 *
 * # Azure EKS example
 *
 * ```sh
 *  $ pulumi import astra:index/privateLinkEndpoint:PrivateLinkEndpoint example a6bc9c26-e7ce-424f-84c7-0a00afb12588/datacenter/a6bc9c26-e7ce-424f-84c7-0a00afb12588-1/endpoint/dc5ee5b1-4fc2-463e-a56b-ff54dd38b879/providers/Microsoft.Network/privateEndpoints/private-endpoint-example
 * ```
 */
export class PrivateLinkEndpoint extends pulumi.CustomResource {
    /**
     * Get an existing PrivateLinkEndpoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PrivateLinkEndpointState, opts?: pulumi.CustomResourceOptions): PrivateLinkEndpoint {
        return new PrivateLinkEndpoint(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'astra:index/privateLinkEndpoint:PrivateLinkEndpoint';

    /**
     * Returns true if the given object is an instance of PrivateLinkEndpoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PrivateLinkEndpoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PrivateLinkEndpoint.__pulumiType;
    }

    /**
     * Endpoint ID for referencing within Astra. May be different than the endpointId of this resource.
     */
    public /*out*/ readonly astraEndpointId!: pulumi.Output<string>;
    /**
     * The ID of the Astra database.
     */
    public readonly databaseId!: pulumi.Output<string>;
    /**
     * Astra datacenter in the region where the private link will be created.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
     */
    public readonly endpointId!: pulumi.Output<string>;

    /**
     * Create a PrivateLinkEndpoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PrivateLinkEndpointArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PrivateLinkEndpointArgs | PrivateLinkEndpointState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PrivateLinkEndpointState | undefined;
            resourceInputs["astraEndpointId"] = state ? state.astraEndpointId : undefined;
            resourceInputs["databaseId"] = state ? state.databaseId : undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["endpointId"] = state ? state.endpointId : undefined;
        } else {
            const args = argsOrState as PrivateLinkEndpointArgs | undefined;
            if ((!args || args.databaseId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'databaseId'");
            }
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.endpointId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'endpointId'");
            }
            resourceInputs["databaseId"] = args ? args.databaseId : undefined;
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["endpointId"] = args ? args.endpointId : undefined;
            resourceInputs["astraEndpointId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PrivateLinkEndpoint.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PrivateLinkEndpoint resources.
 */
export interface PrivateLinkEndpointState {
    /**
     * Endpoint ID for referencing within Astra. May be different than the endpointId of this resource.
     */
    astraEndpointId?: pulumi.Input<string>;
    /**
     * The ID of the Astra database.
     */
    databaseId?: pulumi.Input<string>;
    /**
     * Astra datacenter in the region where the private link will be created.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
     */
    endpointId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PrivateLinkEndpoint resource.
 */
export interface PrivateLinkEndpointArgs {
    /**
     * The ID of the Astra database.
     */
    databaseId: pulumi.Input<string>;
    /**
     * Astra datacenter in the region where the private link will be created.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
     */
    endpointId: pulumi.Input<string>;
}
