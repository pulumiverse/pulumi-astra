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
    public static class GetPrivateLinks
    {
        /// <summary>
        /// `astra.getPrivateLinks` provides a datasource that lists the private links in an Astra database.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Astra = Pulumi.Astra;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var dev = Astra.GetPrivateLinks.Invoke(new()
        ///     {
        ///         DatabaseId = "a6bc9c26-e7ce-424f-84c7-0a00afb12588",
        ///         DatacenterId = "a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetPrivateLinksResult> InvokeAsync(GetPrivateLinksArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPrivateLinksResult>("astra:index/getPrivateLinks:getPrivateLinks", args ?? new GetPrivateLinksArgs(), options.WithDefaults());

        /// <summary>
        /// `astra.getPrivateLinks` provides a datasource that lists the private links in an Astra database.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Astra = Pulumi.Astra;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var dev = Astra.GetPrivateLinks.Invoke(new()
        ///     {
        ///         DatabaseId = "a6bc9c26-e7ce-424f-84c7-0a00afb12588",
        ///         DatacenterId = "a6bc9c26-e7ce-424f-84c7-0a00afb12588-1",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetPrivateLinksResult> Invoke(GetPrivateLinksInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPrivateLinksResult>("astra:index/getPrivateLinks:getPrivateLinks", args ?? new GetPrivateLinksInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPrivateLinksArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the Astra database.
        /// </summary>
        [Input("databaseId", required: true)]
        public string DatabaseId { get; set; } = null!;

        /// <summary>
        /// The datacenter where of the Astra database.
        /// </summary>
        [Input("datacenterId", required: true)]
        public string DatacenterId { get; set; } = null!;

        public GetPrivateLinksArgs()
        {
        }
        public static new GetPrivateLinksArgs Empty => new GetPrivateLinksArgs();
    }

    public sealed class GetPrivateLinksInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the Astra database.
        /// </summary>
        [Input("databaseId", required: true)]
        public Input<string> DatabaseId { get; set; } = null!;

        /// <summary>
        /// The datacenter where of the Astra database.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        public GetPrivateLinksInvokeArgs()
        {
        }
        public static new GetPrivateLinksInvokeArgs Empty => new GetPrivateLinksInvokeArgs();
    }


    [OutputType]
    public sealed class GetPrivateLinksResult
    {
        /// <summary>
        /// The ID of the Astra database.
        /// </summary>
        public readonly string DatabaseId;
        /// <summary>
        /// The datacenter where of the Astra database.
        /// </summary>
        public readonly string DatacenterId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The list of private links that match the search criteria.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPrivateLinksResultResult> Results;

        [OutputConstructor]
        private GetPrivateLinksResult(
            string databaseId,

            string datacenterId,

            string id,

            ImmutableArray<Outputs.GetPrivateLinksResultResult> results)
        {
            DatabaseId = databaseId;
            DatacenterId = datacenterId;
            Id = id;
            Results = results;
        }
    }
}
