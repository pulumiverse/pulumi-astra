// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package astra

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// `getRoles` provides a datasource for a list of Astra roles. This can be used to select roles within your Astra Organization.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/pulumiverse/pulumi-astra/sdk/go/astra"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := astra.LookupRoles(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupRoles(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*LookupRolesResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupRolesResult
	err := ctx.Invoke("astra:index/getRoles:getRoles", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getRoles.
type LookupRolesResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The list of Astra roles.
	Results []GetRolesResult `pulumi:"results"`
}
