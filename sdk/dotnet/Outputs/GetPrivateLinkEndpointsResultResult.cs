// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Astra.Outputs
{

    [OutputType]
    public sealed class GetPrivateLinkEndpointsResultResult
    {
        public readonly string CreateTime;
        public readonly string Description;
        /// <summary>
        /// Endpoint ID.
        /// </summary>
        public readonly string EndpointId;
        public readonly string Status;

        [OutputConstructor]
        private GetPrivateLinkEndpointsResultResult(
            string createTime,

            string description,

            string endpointId,

            string status)
        {
            CreateTime = createTime;
            Description = description;
            EndpointId = endpointId;
            Status = status;
        }
    }
}
