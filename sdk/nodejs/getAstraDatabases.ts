// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * `astra.getAstraDatabases` provides a datasource for a list of Astra databases. This can be used to select databases within your Astra Organization.
 */
export function getAstraDatabases(args?: GetAstraDatabasesArgs, opts?: pulumi.InvokeOptions): Promise<GetAstraDatabasesResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("astra:index/getAstraDatabases:getAstraDatabases", {
        "cloudProvider": args.cloudProvider,
        "status": args.status,
    }, opts);
}

/**
 * A collection of arguments for invoking getAstraDatabases.
 */
export interface GetAstraDatabasesArgs {
    cloudProvider?: string;
    status?: string;
}

/**
 * A collection of values returned by getAstraDatabases.
 */
export interface GetAstraDatabasesResult {
    readonly cloudProvider?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly results: outputs.GetAstraDatabasesResult[];
    readonly status?: string;
}

export function getAstraDatabasesOutput(args?: GetAstraDatabasesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAstraDatabasesResult> {
    return pulumi.output(args).apply(a => getAstraDatabases(a, opts))
}

/**
 * A collection of arguments for invoking getAstraDatabases.
 */
export interface GetAstraDatabasesOutputArgs {
    cloudProvider?: pulumi.Input<string>;
    status?: pulumi.Input<string>;
}