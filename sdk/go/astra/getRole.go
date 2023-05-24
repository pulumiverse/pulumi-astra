// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package astra

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// `Role` provides a datasource that lists the custom roles for an org.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-astra/sdk/go/astra"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/pulumiverse/pulumi-astra/sdk/go/astra"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := astra.LookupRole(ctx, &GetRoleArgs{
// 			RoleId: "role-id-here",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupRole(ctx *pulumi.Context, args *LookupRoleArgs, opts ...pulumi.InvokeOption) (*LookupRoleResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupRoleResult
	err := ctx.Invoke("astra:index/getRole:getRole", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getRole.
type LookupRoleArgs struct {
	// Role ID, system generated
	RoleId string `pulumi:"roleId"`
}

// A collection of values returned by getRole.
type LookupRoleResult struct {
	// Role description
	Description string `pulumi:"description"`
	// Role effect
	Effect string `pulumi:"effect"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// List of policies for the role. See https://docs.datastax.com/en/astra/docs/user-permissions.html#*operational*roles_detail for supported policies.
	Policies []string `pulumi:"policies"`
	// Resources for which role is applicable (format is "drn:astra:org:\n\n", followed by optional resource criteria. See example usage above).
	Resources []string `pulumi:"resources"`
	// Role ID, system generated
	RoleId string `pulumi:"roleId"`
	// Role name
	RoleName string `pulumi:"roleName"`
}

func LookupRoleOutput(ctx *pulumi.Context, args LookupRoleOutputArgs, opts ...pulumi.InvokeOption) LookupRoleResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupRoleResult, error) {
			args := v.(LookupRoleArgs)
			r, err := LookupRole(ctx, &args, opts...)
			var s LookupRoleResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupRoleResultOutput)
}

// A collection of arguments for invoking getRole.
type LookupRoleOutputArgs struct {
	// Role ID, system generated
	RoleId pulumi.StringInput `pulumi:"roleId"`
}

func (LookupRoleOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRoleArgs)(nil)).Elem()
}

// A collection of values returned by getRole.
type LookupRoleResultOutput struct{ *pulumi.OutputState }

func (LookupRoleResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRoleResult)(nil)).Elem()
}

func (o LookupRoleResultOutput) ToLookupRoleResultOutput() LookupRoleResultOutput {
	return o
}

func (o LookupRoleResultOutput) ToLookupRoleResultOutputWithContext(ctx context.Context) LookupRoleResultOutput {
	return o
}

// Role description
func (o LookupRoleResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRoleResult) string { return v.Description }).(pulumi.StringOutput)
}

// Role effect
func (o LookupRoleResultOutput) Effect() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRoleResult) string { return v.Effect }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupRoleResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRoleResult) string { return v.Id }).(pulumi.StringOutput)
}

// List of policies for the role. See https://docs.datastax.com/en/astra/docs/user-permissions.html#*operational*roles_detail for supported policies.
func (o LookupRoleResultOutput) Policies() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupRoleResult) []string { return v.Policies }).(pulumi.StringArrayOutput)
}

// Resources for which role is applicable (format is "drn:astra:org:\n\n", followed by optional resource criteria. See example usage above).
func (o LookupRoleResultOutput) Resources() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupRoleResult) []string { return v.Resources }).(pulumi.StringArrayOutput)
}

// Role ID, system generated
func (o LookupRoleResultOutput) RoleId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRoleResult) string { return v.RoleId }).(pulumi.StringOutput)
}

// Role name
func (o LookupRoleResultOutput) RoleName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRoleResult) string { return v.RoleName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupRoleResultOutput{})
}
