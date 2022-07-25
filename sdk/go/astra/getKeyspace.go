// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package astra

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// `Keyspace` provides a datasource for a particular keyspace. See `getKeyspaces` if you're looking to fetch all the keyspaces for a particular database.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-astra/sdk/go/astra"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/pulumiverse/pulumi-index/sdk/go/index"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := astra.LookupKeyspace(ctx, &GetKeyspaceArgs{
// 			DatabaseId: "f9f4b1e0-4c05-451e-9bba-d631295a7f73",
// 			Name:       "puppies",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupKeyspace(ctx *pulumi.Context, args *LookupKeyspaceArgs, opts ...pulumi.InvokeOption) (*LookupKeyspaceResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupKeyspaceResult
	err := ctx.Invoke("astra:index/getKeyspace:getKeyspace", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getKeyspace.
type LookupKeyspaceArgs struct {
	DatabaseId string `pulumi:"databaseId"`
	Name       string `pulumi:"name"`
}

// A collection of values returned by getKeyspace.
type LookupKeyspaceResult struct {
	DatabaseId string `pulumi:"databaseId"`
	// The provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
}

func LookupKeyspaceOutput(ctx *pulumi.Context, args LookupKeyspaceOutputArgs, opts ...pulumi.InvokeOption) LookupKeyspaceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupKeyspaceResult, error) {
			args := v.(LookupKeyspaceArgs)
			r, err := LookupKeyspace(ctx, &args, opts...)
			var s LookupKeyspaceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupKeyspaceResultOutput)
}

// A collection of arguments for invoking getKeyspace.
type LookupKeyspaceOutputArgs struct {
	DatabaseId pulumi.StringInput `pulumi:"databaseId"`
	Name       pulumi.StringInput `pulumi:"name"`
}

func (LookupKeyspaceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupKeyspaceArgs)(nil)).Elem()
}

// A collection of values returned by getKeyspace.
type LookupKeyspaceResultOutput struct{ *pulumi.OutputState }

func (LookupKeyspaceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupKeyspaceResult)(nil)).Elem()
}

func (o LookupKeyspaceResultOutput) ToLookupKeyspaceResultOutput() LookupKeyspaceResultOutput {
	return o
}

func (o LookupKeyspaceResultOutput) ToLookupKeyspaceResultOutputWithContext(ctx context.Context) LookupKeyspaceResultOutput {
	return o
}

func (o LookupKeyspaceResultOutput) DatabaseId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKeyspaceResult) string { return v.DatabaseId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupKeyspaceResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKeyspaceResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupKeyspaceResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKeyspaceResult) string { return v.Name }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupKeyspaceResultOutput{})
}