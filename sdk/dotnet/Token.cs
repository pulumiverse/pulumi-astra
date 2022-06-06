// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Astra
{
    /// <summary>
    /// `astra.Token` resource represents a token with a specific role assigned.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Astra = Pulumi.Astra;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Astra.Token("example", new Astra.TokenArgs
    ///         {
    ///             Roles = 
    ///             {
    ///                 "a8cd363d-5069-4a2b-86d8-0578139812ac",
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import astra:index/token:Token example client-secret
    /// ```
    /// </summary>
    [AstraResourceType("astra:index/token:Token")]
    public partial class Token : Pulumi.CustomResource
    {
        /// <summary>
        /// Client id, use as username in cql to connect
        /// </summary>
        [Output("clientId")]
        public Output<string> ClientId { get; private set; } = null!;

        /// <summary>
        /// List of Role IDs to be assigned to the generated token
        /// </summary>
        [Output("roles")]
        public Output<ImmutableArray<string>> Roles { get; private set; } = null!;

        /// <summary>
        /// Secret, use as password in cql to connect
        /// </summary>
        [Output("secret")]
        public Output<string> Secret { get; private set; } = null!;

        /// <summary>
        /// Token, use as auth bearer for API calls or as password in combination with the word `token` in cql
        /// </summary>
        [Output("token")]
        public Output<string> AstraToken { get; private set; } = null!;


        /// <summary>
        /// Create a Token resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Token(string name, TokenArgs args, CustomResourceOptions? options = null)
            : base("astra:index/token:Token", name, args ?? new TokenArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Token(string name, Input<string> id, TokenState? state = null, CustomResourceOptions? options = null)
            : base("astra:index/token:Token", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Token resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Token Get(string name, Input<string> id, TokenState? state = null, CustomResourceOptions? options = null)
        {
            return new Token(name, id, state, options);
        }
    }

    public sealed class TokenArgs : Pulumi.ResourceArgs
    {
        [Input("roles", required: true)]
        private InputList<string>? _roles;

        /// <summary>
        /// List of Role IDs to be assigned to the generated token
        /// </summary>
        public InputList<string> Roles
        {
            get => _roles ?? (_roles = new InputList<string>());
            set => _roles = value;
        }

        public TokenArgs()
        {
        }
    }

    public sealed class TokenState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Client id, use as username in cql to connect
        /// </summary>
        [Input("clientId")]
        public Input<string>? ClientId { get; set; }

        [Input("roles")]
        private InputList<string>? _roles;

        /// <summary>
        /// List of Role IDs to be assigned to the generated token
        /// </summary>
        public InputList<string> Roles
        {
            get => _roles ?? (_roles = new InputList<string>());
            set => _roles = value;
        }

        /// <summary>
        /// Secret, use as password in cql to connect
        /// </summary>
        [Input("secret")]
        public Input<string>? Secret { get; set; }

        /// <summary>
        /// Token, use as auth bearer for API calls or as password in combination with the word `token` in cql
        /// </summary>
        [Input("token")]
        public Input<string>? AstraToken { get; set; }

        public TokenState()
        {
        }
    }
}
