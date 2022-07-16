// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Astra
{
    /// <summary>
    /// `astra.StreamingTenant` creates an Astra Streaming tenant.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Astra = Pulumiverse.Astra;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var streamingTenant_1 = new Astra.StreamingTenant("streamingTenant-1", new Astra.StreamingTenantArgs
    ///         {
    ///             CloudProvider = "gcp",
    ///             Region = "useast-4",
    ///             TenantName = "terraformtest",
    ///             Topic = "terraformtest",
    ///             UserEmail = "seb@datastax.com",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import astra:index/streamingTenant:StreamingTenant example tenant_name
    /// ```
    /// </summary>
    [AstraResourceType("astra:index/streamingTenant:StreamingTenant")]
    public partial class StreamingTenant : Pulumi.CustomResource
    {
        /// <summary>
        /// Cloud provider
        /// </summary>
        [Output("cloudProvider")]
        public Output<string> CloudProvider { get; private set; } = null!;

        /// <summary>
        /// cloud region
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// Streaming tenant name.
        /// </summary>
        [Output("tenantName")]
        public Output<string> TenantName { get; private set; } = null!;

        /// <summary>
        /// Streaming tenant topic.
        /// </summary>
        [Output("topic")]
        public Output<string> Topic { get; private set; } = null!;

        /// <summary>
        /// User email for tenant.
        /// </summary>
        [Output("userEmail")]
        public Output<string> UserEmail { get; private set; } = null!;


        /// <summary>
        /// Create a StreamingTenant resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public StreamingTenant(string name, StreamingTenantArgs args, CustomResourceOptions? options = null)
            : base("astra:index/streamingTenant:StreamingTenant", name, args ?? new StreamingTenantArgs(), MakeResourceOptions(options, ""))
        {
        }

        private StreamingTenant(string name, Input<string> id, StreamingTenantState? state = null, CustomResourceOptions? options = null)
            : base("astra:index/streamingTenant:StreamingTenant", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/pulumiverse/pulumi-astra/releases/download/${VERSION}",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing StreamingTenant resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static StreamingTenant Get(string name, Input<string> id, StreamingTenantState? state = null, CustomResourceOptions? options = null)
        {
            return new StreamingTenant(name, id, state, options);
        }
    }

    public sealed class StreamingTenantArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Cloud provider
        /// </summary>
        [Input("cloudProvider", required: true)]
        public Input<string> CloudProvider { get; set; } = null!;

        /// <summary>
        /// cloud region
        /// </summary>
        [Input("region", required: true)]
        public Input<string> Region { get; set; } = null!;

        /// <summary>
        /// Streaming tenant name.
        /// </summary>
        [Input("tenantName", required: true)]
        public Input<string> TenantName { get; set; } = null!;

        /// <summary>
        /// Streaming tenant topic.
        /// </summary>
        [Input("topic", required: true)]
        public Input<string> Topic { get; set; } = null!;

        /// <summary>
        /// User email for tenant.
        /// </summary>
        [Input("userEmail", required: true)]
        public Input<string> UserEmail { get; set; } = null!;

        public StreamingTenantArgs()
        {
        }
    }

    public sealed class StreamingTenantState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Cloud provider
        /// </summary>
        [Input("cloudProvider")]
        public Input<string>? CloudProvider { get; set; }

        /// <summary>
        /// cloud region
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Streaming tenant name.
        /// </summary>
        [Input("tenantName")]
        public Input<string>? TenantName { get; set; }

        /// <summary>
        /// Streaming tenant topic.
        /// </summary>
        [Input("topic")]
        public Input<string>? Topic { get; set; }

        /// <summary>
        /// User email for tenant.
        /// </summary>
        [Input("userEmail")]
        public Input<string>? UserEmail { get; set; }

        public StreamingTenantState()
        {
        }
    }
}
