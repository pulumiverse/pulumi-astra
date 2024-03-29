// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * `astra.StreamingTenant` creates an Astra Streaming tenant.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as astra from "@pulumi/astra";
 *
 * const streaming_tenant_1 = new astra.StreamingTenant("streaming_tenant-1", {
 *     cloudProvider: "gcp",
 *     region: "useast-4",
 *     tenantName: "terraformtest",
 *     topic: "terraformtest",
 *     userEmail: "seb@datastax.com",
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import astra:index/streamingTenant:StreamingTenant example tenant_name
 * ```
 */
export class StreamingTenant extends pulumi.CustomResource {
    /**
     * Get an existing StreamingTenant resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StreamingTenantState, opts?: pulumi.CustomResourceOptions): StreamingTenant {
        return new StreamingTenant(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'astra:index/streamingTenant:StreamingTenant';

    /**
     * Returns true if the given object is an instance of StreamingTenant.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is StreamingTenant {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === StreamingTenant.__pulumiType;
    }

    /**
     * The Pulsar Binary Protocol URL used for production and consumption of messages.
     */
    public /*out*/ readonly brokerServiceUrl!: pulumi.Output<string>;
    /**
     * Cloud provider
     */
    public readonly cloudProvider!: pulumi.Output<string>;
    /**
     * Pulsar cluster name.
     */
    public /*out*/ readonly clusterName!: pulumi.Output<string>;
    /**
     * Whether or not to allow Terraform to destroy this tenant. Unless this field is set to false in Terraform state, a
     * `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
     */
    public readonly deletionProtection!: pulumi.Output<boolean | undefined>;
    /**
     * cloud region
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * UUID for the tenant.
     */
    public /*out*/ readonly tenantId!: pulumi.Output<string>;
    /**
     * Streaming tenant name.
     */
    public readonly tenantName!: pulumi.Output<string>;
    /**
     * Streaming tenant topic.
     */
    public readonly topic!: pulumi.Output<string>;
    /**
     * User email for tenant.
     */
    public readonly userEmail!: pulumi.Output<string>;
    /**
     * URL for metrics.
     */
    public /*out*/ readonly userMetricsUrl!: pulumi.Output<string>;
    /**
     * URL used for administrative operations.
     */
    public /*out*/ readonly webServiceUrl!: pulumi.Output<string>;
    /**
     * URL used for web socket query parameter operations.
     */
    public /*out*/ readonly webSocketQueryParamUrl!: pulumi.Output<string>;
    /**
     * URL used for web socket operations.
     */
    public /*out*/ readonly webSocketUrl!: pulumi.Output<string>;

    /**
     * Create a StreamingTenant resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StreamingTenantArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: StreamingTenantArgs | StreamingTenantState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as StreamingTenantState | undefined;
            resourceInputs["brokerServiceUrl"] = state ? state.brokerServiceUrl : undefined;
            resourceInputs["cloudProvider"] = state ? state.cloudProvider : undefined;
            resourceInputs["clusterName"] = state ? state.clusterName : undefined;
            resourceInputs["deletionProtection"] = state ? state.deletionProtection : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["tenantId"] = state ? state.tenantId : undefined;
            resourceInputs["tenantName"] = state ? state.tenantName : undefined;
            resourceInputs["topic"] = state ? state.topic : undefined;
            resourceInputs["userEmail"] = state ? state.userEmail : undefined;
            resourceInputs["userMetricsUrl"] = state ? state.userMetricsUrl : undefined;
            resourceInputs["webServiceUrl"] = state ? state.webServiceUrl : undefined;
            resourceInputs["webSocketQueryParamUrl"] = state ? state.webSocketQueryParamUrl : undefined;
            resourceInputs["webSocketUrl"] = state ? state.webSocketUrl : undefined;
        } else {
            const args = argsOrState as StreamingTenantArgs | undefined;
            if ((!args || args.cloudProvider === undefined) && !opts.urn) {
                throw new Error("Missing required property 'cloudProvider'");
            }
            if ((!args || args.region === undefined) && !opts.urn) {
                throw new Error("Missing required property 'region'");
            }
            if ((!args || args.tenantName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tenantName'");
            }
            if ((!args || args.topic === undefined) && !opts.urn) {
                throw new Error("Missing required property 'topic'");
            }
            if ((!args || args.userEmail === undefined) && !opts.urn) {
                throw new Error("Missing required property 'userEmail'");
            }
            resourceInputs["cloudProvider"] = args ? args.cloudProvider : undefined;
            resourceInputs["deletionProtection"] = args ? args.deletionProtection : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["tenantName"] = args ? args.tenantName : undefined;
            resourceInputs["topic"] = args ? args.topic : undefined;
            resourceInputs["userEmail"] = args ? args.userEmail : undefined;
            resourceInputs["brokerServiceUrl"] = undefined /*out*/;
            resourceInputs["clusterName"] = undefined /*out*/;
            resourceInputs["tenantId"] = undefined /*out*/;
            resourceInputs["userMetricsUrl"] = undefined /*out*/;
            resourceInputs["webServiceUrl"] = undefined /*out*/;
            resourceInputs["webSocketQueryParamUrl"] = undefined /*out*/;
            resourceInputs["webSocketUrl"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(StreamingTenant.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering StreamingTenant resources.
 */
export interface StreamingTenantState {
    /**
     * The Pulsar Binary Protocol URL used for production and consumption of messages.
     */
    brokerServiceUrl?: pulumi.Input<string>;
    /**
     * Cloud provider
     */
    cloudProvider?: pulumi.Input<string>;
    /**
     * Pulsar cluster name.
     */
    clusterName?: pulumi.Input<string>;
    /**
     * Whether or not to allow Terraform to destroy this tenant. Unless this field is set to false in Terraform state, a
     * `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
     */
    deletionProtection?: pulumi.Input<boolean>;
    /**
     * cloud region
     */
    region?: pulumi.Input<string>;
    /**
     * UUID for the tenant.
     */
    tenantId?: pulumi.Input<string>;
    /**
     * Streaming tenant name.
     */
    tenantName?: pulumi.Input<string>;
    /**
     * Streaming tenant topic.
     */
    topic?: pulumi.Input<string>;
    /**
     * User email for tenant.
     */
    userEmail?: pulumi.Input<string>;
    /**
     * URL for metrics.
     */
    userMetricsUrl?: pulumi.Input<string>;
    /**
     * URL used for administrative operations.
     */
    webServiceUrl?: pulumi.Input<string>;
    /**
     * URL used for web socket query parameter operations.
     */
    webSocketQueryParamUrl?: pulumi.Input<string>;
    /**
     * URL used for web socket operations.
     */
    webSocketUrl?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a StreamingTenant resource.
 */
export interface StreamingTenantArgs {
    /**
     * Cloud provider
     */
    cloudProvider: pulumi.Input<string>;
    /**
     * Whether or not to allow Terraform to destroy this tenant. Unless this field is set to false in Terraform state, a
     * `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
     */
    deletionProtection?: pulumi.Input<boolean>;
    /**
     * cloud region
     */
    region: pulumi.Input<string>;
    /**
     * Streaming tenant name.
     */
    tenantName: pulumi.Input<string>;
    /**
     * Streaming tenant topic.
     */
    topic: pulumi.Input<string>;
    /**
     * User email for tenant.
     */
    userEmail: pulumi.Input<string>;
}
