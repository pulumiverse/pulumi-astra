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
    public sealed class GetUsersUserResult
    {
        public readonly string Email;
        public readonly ImmutableArray<Outputs.GetUsersUserRoleResult> Roles;
        public readonly string Status;
        public readonly string UserId;

        [OutputConstructor]
        private GetUsersUserResult(
            string email,

            ImmutableArray<Outputs.GetUsersUserRoleResult> roles,

            string status,

            string userId)
        {
            Email = email;
            Roles = roles;
            Status = status;
            UserId = userId;
        }
    }
}