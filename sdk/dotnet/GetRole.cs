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
    public static class GetRole
    {
        /// <summary>
        /// `astra.Role` provides a datasource that lists the custom roles for an org.
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
        ///     var dev = Astra.GetRole.Invoke(new()
        ///     {
        ///         RoleId = "role-id-here",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetRoleResult> InvokeAsync(GetRoleArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRoleResult>("astra:index/getRole:getRole", args ?? new GetRoleArgs(), options.WithDefaults());

        /// <summary>
        /// `astra.Role` provides a datasource that lists the custom roles for an org.
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
        ///     var dev = Astra.GetRole.Invoke(new()
        ///     {
        ///         RoleId = "role-id-here",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetRoleResult> Invoke(GetRoleInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetRoleResult>("astra:index/getRole:getRole", args ?? new GetRoleInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRoleArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Role ID, system generated
        /// </summary>
        [Input("roleId", required: true)]
        public string RoleId { get; set; } = null!;

        public GetRoleArgs()
        {
        }
        public static new GetRoleArgs Empty => new GetRoleArgs();
    }

    public sealed class GetRoleInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Role ID, system generated
        /// </summary>
        [Input("roleId", required: true)]
        public Input<string> RoleId { get; set; } = null!;

        public GetRoleInvokeArgs()
        {
        }
        public static new GetRoleInvokeArgs Empty => new GetRoleInvokeArgs();
    }


    [OutputType]
    public sealed class GetRoleResult
    {
        /// <summary>
        /// Role description
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Role effect
        /// </summary>
        public readonly string Effect;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// List of policies for the role. See https://docs.datastax.com/en/astra/docs/user-permissions.html#*operational*roles_detail for supported policies.
        /// </summary>
        public readonly ImmutableArray<string> Policies;
        /// <summary>
        /// Resources for which role is applicable (format is "drn:astra:org:\n\n", followed by optional resource criteria. See example usage above).
        /// </summary>
        public readonly ImmutableArray<string> Resources;
        /// <summary>
        /// Role ID, system generated
        /// </summary>
        public readonly string RoleId;
        /// <summary>
        /// Role name
        /// </summary>
        public readonly string RoleName;

        [OutputConstructor]
        private GetRoleResult(
            string description,

            string effect,

            string id,

            ImmutableArray<string> policies,

            ImmutableArray<string> resources,

            string roleId,

            string roleName)
        {
            Description = description;
            Effect = effect;
            Id = id;
            Policies = policies;
            Resources = resources;
            RoleId = roleId;
            RoleName = roleName;
        }
    }
}
