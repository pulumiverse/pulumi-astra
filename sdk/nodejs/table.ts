// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * `astra.Table` provides a table resource which represents a table in cassandra.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as astra from "@pulumiverse/astra";
 *
 * const dev = new astra.Database("dev", {
 *     keyspace: "puppies",
 *     cloudProvider: "gcp",
 *     regions: ["us-east1"],
 * });
 * const table_1 = new astra.Table("table-1", {
 *     table: "mytable",
 *     keyspace: "puppies",
 *     databaseId: dev.id,
 *     region: "us-east1",
 *     clusteringColumns: "a:b",
 *     partitionKeys: "c:d",
 *     columnDefinitions: [
 *         {
 *             Name: "a",
 *             Static: "false",
 *             TypeDefinition: "text",
 *         },
 *         {
 *             Name: "b",
 *             Static: "false",
 *             TypeDefinition: "text",
 *         },
 *         {
 *             Name: "c",
 *             Static: "false",
 *             TypeDefinition: "text",
 *         },
 *         {
 *             Name: "d",
 *             Static: "false",
 *             TypeDefinition: "text",
 *         },
 *         {
 *             Name: "e",
 *             Static: "false",
 *             TypeDefinition: "text",
 *         },
 *         {
 *             Name: "f",
 *             Static: "false",
 *             TypeDefinition: "text",
 *         },
 *     ],
 * });
 * ```
 *
 * ## Import
 *
 * # the import id includes the database_id, keyspace name, and table name.
 *
 * ```sh
 *  $ pulumi import astra:index/table:Table example 48bfc13b-c1a5-48db-b70f-b6ef9709872b/kayspacename/tablename
 * ```
 */
export class Table extends pulumi.CustomResource {
    /**
     * Get an existing Table resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableState, opts?: pulumi.CustomResourceOptions): Table {
        return new Table(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'astra:index/table:Table';

    /**
     * Returns true if the given object is an instance of Table.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Table {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Table.__pulumiType;
    }

    /**
     * Clustering column(s), separated by :
     */
    public readonly clusteringColumns!: pulumi.Output<string>;
    /**
     * A list of table Definitions
     */
    public readonly columnDefinitions!: pulumi.Output<{[key: string]: string}[]>;
    /**
     * Astra database to create the keyspace.
     */
    public readonly databaseId!: pulumi.Output<string>;
    /**
     * Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters are supported as the first character.
     */
    public readonly keyspace!: pulumi.Output<string>;
    /**
     * Partition key(s), separated by :
     */
    public readonly partitionKeys!: pulumi.Output<string>;
    /**
     * region.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * Table name can have up to 48 alpha-numeric characters and contain underscores; only letters are supported as the first character.
     */
    public readonly table!: pulumi.Output<string>;

    /**
     * Create a Table resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TableArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TableArgs | TableState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TableState | undefined;
            resourceInputs["clusteringColumns"] = state ? state.clusteringColumns : undefined;
            resourceInputs["columnDefinitions"] = state ? state.columnDefinitions : undefined;
            resourceInputs["databaseId"] = state ? state.databaseId : undefined;
            resourceInputs["keyspace"] = state ? state.keyspace : undefined;
            resourceInputs["partitionKeys"] = state ? state.partitionKeys : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["table"] = state ? state.table : undefined;
        } else {
            const args = argsOrState as TableArgs | undefined;
            if ((!args || args.clusteringColumns === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusteringColumns'");
            }
            if ((!args || args.columnDefinitions === undefined) && !opts.urn) {
                throw new Error("Missing required property 'columnDefinitions'");
            }
            if ((!args || args.databaseId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'databaseId'");
            }
            if ((!args || args.keyspace === undefined) && !opts.urn) {
                throw new Error("Missing required property 'keyspace'");
            }
            if ((!args || args.partitionKeys === undefined) && !opts.urn) {
                throw new Error("Missing required property 'partitionKeys'");
            }
            if ((!args || args.region === undefined) && !opts.urn) {
                throw new Error("Missing required property 'region'");
            }
            if ((!args || args.table === undefined) && !opts.urn) {
                throw new Error("Missing required property 'table'");
            }
            resourceInputs["clusteringColumns"] = args ? args.clusteringColumns : undefined;
            resourceInputs["columnDefinitions"] = args ? args.columnDefinitions : undefined;
            resourceInputs["databaseId"] = args ? args.databaseId : undefined;
            resourceInputs["keyspace"] = args ? args.keyspace : undefined;
            resourceInputs["partitionKeys"] = args ? args.partitionKeys : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["table"] = args ? args.table : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Table.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Table resources.
 */
export interface TableState {
    /**
     * Clustering column(s), separated by :
     */
    clusteringColumns?: pulumi.Input<string>;
    /**
     * A list of table Definitions
     */
    columnDefinitions?: pulumi.Input<pulumi.Input<{[key: string]: pulumi.Input<string>}>[]>;
    /**
     * Astra database to create the keyspace.
     */
    databaseId?: pulumi.Input<string>;
    /**
     * Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters are supported as the first character.
     */
    keyspace?: pulumi.Input<string>;
    /**
     * Partition key(s), separated by :
     */
    partitionKeys?: pulumi.Input<string>;
    /**
     * region.
     */
    region?: pulumi.Input<string>;
    /**
     * Table name can have up to 48 alpha-numeric characters and contain underscores; only letters are supported as the first character.
     */
    table?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Table resource.
 */
export interface TableArgs {
    /**
     * Clustering column(s), separated by :
     */
    clusteringColumns: pulumi.Input<string>;
    /**
     * A list of table Definitions
     */
    columnDefinitions: pulumi.Input<pulumi.Input<{[key: string]: pulumi.Input<string>}>[]>;
    /**
     * Astra database to create the keyspace.
     */
    databaseId: pulumi.Input<string>;
    /**
     * Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters are supported as the first character.
     */
    keyspace: pulumi.Input<string>;
    /**
     * Partition key(s), separated by :
     */
    partitionKeys: pulumi.Input<string>;
    /**
     * region.
     */
    region: pulumi.Input<string>;
    /**
     * Table name can have up to 48 alpha-numeric characters and contain underscores; only letters are supported as the first character.
     */
    table: pulumi.Input<string>;
}
