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
    public static class GetAstraDatabase
    {
        /// <summary>
        /// `astra.Database` provides a datasource for Astra an Astra database. This can be used to select an existing database within your Astra Organization.
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
        ///     var db = Astra.GetAstraDatabase.Invoke(new()
        ///     {
        ///         DatabaseId = "8d356587-73b3-430a-9c0e-d780332e2afb",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetAstraDatabaseResult> InvokeAsync(GetAstraDatabaseArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetAstraDatabaseResult>("astra:index/getAstraDatabase:getAstraDatabase", args ?? new GetAstraDatabaseArgs(), options.WithDefaults());

        /// <summary>
        /// `astra.Database` provides a datasource for Astra an Astra database. This can be used to select an existing database within your Astra Organization.
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
        ///     var db = Astra.GetAstraDatabase.Invoke(new()
        ///     {
        ///         DatabaseId = "8d356587-73b3-430a-9c0e-d780332e2afb",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetAstraDatabaseResult> Invoke(GetAstraDatabaseInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetAstraDatabaseResult>("astra:index/getAstraDatabase:getAstraDatabase", args ?? new GetAstraDatabaseInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAstraDatabaseArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Astra Database ID (system generated)
        /// </summary>
        [Input("databaseId", required: true)]
        public string DatabaseId { get; set; } = null!;

        public GetAstraDatabaseArgs()
        {
        }
        public static new GetAstraDatabaseArgs Empty => new GetAstraDatabaseArgs();
    }

    public sealed class GetAstraDatabaseInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Astra Database ID (system generated)
        /// </summary>
        [Input("databaseId", required: true)]
        public Input<string> DatabaseId { get; set; } = null!;

        public GetAstraDatabaseInvokeArgs()
        {
        }
        public static new GetAstraDatabaseInvokeArgs Empty => new GetAstraDatabaseInvokeArgs();
    }


    [OutputType]
    public sealed class GetAstraDatabaseResult
    {
        /// <summary>
        /// Additional keyspaces
        /// </summary>
        public readonly ImmutableArray<string> AdditionalKeyspaces;
        /// <summary>
        /// Cloud provider (AWS, GCP, AZURE)
        /// </summary>
        public readonly string CloudProvider;
        /// <summary>
        /// URL for cqlsh web
        /// </summary>
        public readonly string CqlshUrl;
        /// <summary>
        /// REST API URL
        /// </summary>
        public readonly string DataEndpointUrl;
        /// <summary>
        /// Astra Database ID (system generated)
        /// </summary>
        public readonly string DatabaseId;
        /// <summary>
        /// Map of Datacenter IDs. The map key is "cloud_provider.region". Example: "GCP.us-east4".
        /// </summary>
        public readonly ImmutableDictionary<string, string> Datacenters;
        /// <summary>
        /// URL for the grafana dashboard for this database
        /// </summary>
        public readonly string GrafanaUrl;
        /// <summary>
        /// Graphql URL
        /// </summary>
        public readonly string GraphqlUrl;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Initial keyspace
        /// </summary>
        public readonly string Keyspace;
        /// <summary>
        /// Database name (user provided)
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Node count (not relevant for serverless databases)
        /// </summary>
        public readonly int NodeCount;
        /// <summary>
        /// Ordg id (system generated)
        /// </summary>
        public readonly string OrganizationId;
        /// <summary>
        /// Owner id (system generated)
        /// </summary>
        public readonly string OwnerId;
        /// <summary>
        /// Cloud provider region. Get list of supported regions from regions data-source
        /// </summary>
        public readonly ImmutableArray<string> Regions;
        /// <summary>
        /// Replication Factor (not relevant for serverless databases)
        /// </summary>
        public readonly int ReplicationFactor;
        /// <summary>
        /// Database status
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// Storage Capacity (not relevant for serverelss databases)
        /// </summary>
        public readonly int TotalStorage;

        [OutputConstructor]
        private GetAstraDatabaseResult(
            ImmutableArray<string> additionalKeyspaces,

            string cloudProvider,

            string cqlshUrl,

            string dataEndpointUrl,

            string databaseId,

            ImmutableDictionary<string, string> datacenters,

            string grafanaUrl,

            string graphqlUrl,

            string id,

            string keyspace,

            string name,

            int nodeCount,

            string organizationId,

            string ownerId,

            ImmutableArray<string> regions,

            int replicationFactor,

            string status,

            int totalStorage)
        {
            AdditionalKeyspaces = additionalKeyspaces;
            CloudProvider = cloudProvider;
            CqlshUrl = cqlshUrl;
            DataEndpointUrl = dataEndpointUrl;
            DatabaseId = databaseId;
            Datacenters = datacenters;
            GrafanaUrl = grafanaUrl;
            GraphqlUrl = graphqlUrl;
            Id = id;
            Keyspace = keyspace;
            Name = name;
            NodeCount = nodeCount;
            OrganizationId = organizationId;
            OwnerId = ownerId;
            Regions = regions;
            ReplicationFactor = replicationFactor;
            Status = status;
            TotalStorage = totalStorage;
        }
    }
}
