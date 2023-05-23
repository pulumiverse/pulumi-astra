// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * `astra.StreamingSink` creates a streaming sink which sends data from a topic to a target system.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as astra from "@pulumiverse/astra";
 *
 * const streamingTenant_1 = new astra.StreamingTenant("streamingTenant-1", {
 *     tenantName: "terraformtest2",
 *     topic: "terraformtest",
 *     region: "useast-4",
 *     cloudProvider: "gcp",
 *     userEmail: "seb@datastax.com",
 * });
 * const cdc_1 = new astra.Cdc("cdc-1", {
 *     databaseId: "5b70892f-e01a-4595-98e6-19ecc9985d50",
 *     databaseName: "sai_test",
 *     table: "test",
 *     keyspace: "sai_test",
 *     topicPartitions: 3,
 *     tenantName: streamingTenant_1.tenantName,
 * }, {
 *     dependsOn: [streamingTenant_1],
 * });
 * const streamingSink_1 = new astra.StreamingSink("streamingSink-1", {
 *     tenantName: streamingTenant_1.tenantName,
 *     topic: cdc_1.dataTopic,
 *     region: "useast-4",
 *     cloudProvider: "gcp",
 *     sinkName: "jdbc-clickhouse",
 *     retainOrdering: true,
 *     processingGuarantees: "ATLEAST_ONCE",
 *     parallelism: 3,
 *     namespace: "default",
 *     sinkConfigs: JSON.stringify({
 *         userName: "clickhouse",
 *         password: "password",
 *         jdbcUrl: "jdbc:clickhouse://fake.clickhouse.url:8123/pulsar_clickhouse_jdbc_sink",
 *         tableName: "pulsar_clickhouse_jdbc_sink",
 *     }),
 *     autoAck: true,
 * }, {
 *     dependsOn: [
 *         streamingTenant_1,
 *         cdc_1,
 *     ],
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import astra:index/streamingSink:StreamingSink example tenant_name/topic
 * ```
 */
export class StreamingSink extends pulumi.CustomResource {
    /**
     * Get an existing StreamingSink resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StreamingSinkState, opts?: pulumi.CustomResourceOptions): StreamingSink {
        return new StreamingSink(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'astra:index/streamingSink:StreamingSink';

    /**
     * Returns true if the given object is an instance of StreamingSink.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is StreamingSink {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === StreamingSink.__pulumiType;
    }

    /**
     * auto ack
     */
    public readonly autoAck!: pulumi.Output<boolean>;
    /**
     * Cloud provider
     */
    public readonly cloudProvider!: pulumi.Output<string>;
    /**
     * Whether or not to allow Terraform to destroy this streaming sink. Unless this field is set to false in Terraform state,
     * a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
     */
    public readonly deletionProtection!: pulumi.Output<boolean | undefined>;
    /**
     * Pulsar Namespace
     */
    public readonly namespace!: pulumi.Output<string>;
    /**
     * Parallelism for Pulsar sink
     */
    public readonly parallelism!: pulumi.Output<number>;
    /**
     * "ATLEAST*ONCE""ATMOST*ONCE""EFFECTIVELY_ONCE".
     */
    public readonly processingGuarantees!: pulumi.Output<string>;
    /**
     * cloud region
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * Retain ordering.
     */
    public readonly retainOrdering!: pulumi.Output<boolean>;
    /**
     * Sink Configs
     */
    public readonly sinkConfigs!: pulumi.Output<string>;
    /**
     * Name of the sink.
     */
    public readonly sinkName!: pulumi.Output<string>;
    /**
     * Streaming tenant name.
     */
    public readonly tenantName!: pulumi.Output<string>;
    /**
     * Streaming tenant topic.
     */
    public readonly topic!: pulumi.Output<string>;

    /**
     * Create a StreamingSink resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StreamingSinkArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: StreamingSinkArgs | StreamingSinkState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as StreamingSinkState | undefined;
            resourceInputs["autoAck"] = state ? state.autoAck : undefined;
            resourceInputs["cloudProvider"] = state ? state.cloudProvider : undefined;
            resourceInputs["deletionProtection"] = state ? state.deletionProtection : undefined;
            resourceInputs["namespace"] = state ? state.namespace : undefined;
            resourceInputs["parallelism"] = state ? state.parallelism : undefined;
            resourceInputs["processingGuarantees"] = state ? state.processingGuarantees : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["retainOrdering"] = state ? state.retainOrdering : undefined;
            resourceInputs["sinkConfigs"] = state ? state.sinkConfigs : undefined;
            resourceInputs["sinkName"] = state ? state.sinkName : undefined;
            resourceInputs["tenantName"] = state ? state.tenantName : undefined;
            resourceInputs["topic"] = state ? state.topic : undefined;
        } else {
            const args = argsOrState as StreamingSinkArgs | undefined;
            if ((!args || args.autoAck === undefined) && !opts.urn) {
                throw new Error("Missing required property 'autoAck'");
            }
            if ((!args || args.cloudProvider === undefined) && !opts.urn) {
                throw new Error("Missing required property 'cloudProvider'");
            }
            if ((!args || args.namespace === undefined) && !opts.urn) {
                throw new Error("Missing required property 'namespace'");
            }
            if ((!args || args.parallelism === undefined) && !opts.urn) {
                throw new Error("Missing required property 'parallelism'");
            }
            if ((!args || args.processingGuarantees === undefined) && !opts.urn) {
                throw new Error("Missing required property 'processingGuarantees'");
            }
            if ((!args || args.region === undefined) && !opts.urn) {
                throw new Error("Missing required property 'region'");
            }
            if ((!args || args.retainOrdering === undefined) && !opts.urn) {
                throw new Error("Missing required property 'retainOrdering'");
            }
            if ((!args || args.sinkConfigs === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sinkConfigs'");
            }
            if ((!args || args.sinkName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sinkName'");
            }
            if ((!args || args.tenantName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tenantName'");
            }
            if ((!args || args.topic === undefined) && !opts.urn) {
                throw new Error("Missing required property 'topic'");
            }
            resourceInputs["autoAck"] = args ? args.autoAck : undefined;
            resourceInputs["cloudProvider"] = args ? args.cloudProvider : undefined;
            resourceInputs["deletionProtection"] = args ? args.deletionProtection : undefined;
            resourceInputs["namespace"] = args ? args.namespace : undefined;
            resourceInputs["parallelism"] = args ? args.parallelism : undefined;
            resourceInputs["processingGuarantees"] = args ? args.processingGuarantees : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["retainOrdering"] = args ? args.retainOrdering : undefined;
            resourceInputs["sinkConfigs"] = args ? args.sinkConfigs : undefined;
            resourceInputs["sinkName"] = args ? args.sinkName : undefined;
            resourceInputs["tenantName"] = args ? args.tenantName : undefined;
            resourceInputs["topic"] = args ? args.topic : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(StreamingSink.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering StreamingSink resources.
 */
export interface StreamingSinkState {
    /**
     * auto ack
     */
    autoAck?: pulumi.Input<boolean>;
    /**
     * Cloud provider
     */
    cloudProvider?: pulumi.Input<string>;
    /**
     * Whether or not to allow Terraform to destroy this streaming sink. Unless this field is set to false in Terraform state,
     * a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
     */
    deletionProtection?: pulumi.Input<boolean>;
    /**
     * Pulsar Namespace
     */
    namespace?: pulumi.Input<string>;
    /**
     * Parallelism for Pulsar sink
     */
    parallelism?: pulumi.Input<number>;
    /**
     * "ATLEAST*ONCE""ATMOST*ONCE""EFFECTIVELY_ONCE".
     */
    processingGuarantees?: pulumi.Input<string>;
    /**
     * cloud region
     */
    region?: pulumi.Input<string>;
    /**
     * Retain ordering.
     */
    retainOrdering?: pulumi.Input<boolean>;
    /**
     * Sink Configs
     */
    sinkConfigs?: pulumi.Input<string>;
    /**
     * Name of the sink.
     */
    sinkName?: pulumi.Input<string>;
    /**
     * Streaming tenant name.
     */
    tenantName?: pulumi.Input<string>;
    /**
     * Streaming tenant topic.
     */
    topic?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a StreamingSink resource.
 */
export interface StreamingSinkArgs {
    /**
     * auto ack
     */
    autoAck: pulumi.Input<boolean>;
    /**
     * Cloud provider
     */
    cloudProvider: pulumi.Input<string>;
    /**
     * Whether or not to allow Terraform to destroy this streaming sink. Unless this field is set to false in Terraform state,
     * a `terraform destroy` or `terraform apply` command that deletes the instance will fail. Defaults to `true`.
     */
    deletionProtection?: pulumi.Input<boolean>;
    /**
     * Pulsar Namespace
     */
    namespace: pulumi.Input<string>;
    /**
     * Parallelism for Pulsar sink
     */
    parallelism: pulumi.Input<number>;
    /**
     * "ATLEAST*ONCE""ATMOST*ONCE""EFFECTIVELY_ONCE".
     */
    processingGuarantees: pulumi.Input<string>;
    /**
     * cloud region
     */
    region: pulumi.Input<string>;
    /**
     * Retain ordering.
     */
    retainOrdering: pulumi.Input<boolean>;
    /**
     * Sink Configs
     */
    sinkConfigs: pulumi.Input<string>;
    /**
     * Name of the sink.
     */
    sinkName: pulumi.Input<string>;
    /**
     * Streaming tenant name.
     */
    tenantName: pulumi.Input<string>;
    /**
     * Streaming tenant topic.
     */
    topic: pulumi.Input<string>;
}