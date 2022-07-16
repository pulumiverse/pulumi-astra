// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package index

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// `StreamingTenant` creates an Astra Streaming tenant.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/pulumiverse/pulumi-index/sdk/go/index"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := astra.NewStreamingTenant(ctx, "streamingTenant-1", &astra.StreamingTenantArgs{
// 			CloudProvider: pulumi.String("gcp"),
// 			Region:        pulumi.String("useast-4"),
// 			TenantName:    pulumi.String("terraformtest"),
// 			Topic:         pulumi.String("terraformtest"),
// 			UserEmail:     pulumi.String("seb@datastax.com"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// ```sh
//  $ pulumi import astra:index/streamingTenant:StreamingTenant example tenant_name
// ```
type StreamingTenant struct {
	pulumi.CustomResourceState

	// Cloud provider
	CloudProvider pulumi.StringOutput `pulumi:"cloudProvider"`
	// cloud region
	Region pulumi.StringOutput `pulumi:"region"`
	// Streaming tenant name.
	TenantName pulumi.StringOutput `pulumi:"tenantName"`
	// Streaming tenant topic.
	Topic pulumi.StringOutput `pulumi:"topic"`
	// User email for tenant.
	UserEmail pulumi.StringOutput `pulumi:"userEmail"`
}

// NewStreamingTenant registers a new resource with the given unique name, arguments, and options.
func NewStreamingTenant(ctx *pulumi.Context,
	name string, args *StreamingTenantArgs, opts ...pulumi.ResourceOption) (*StreamingTenant, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CloudProvider == nil {
		return nil, errors.New("invalid value for required argument 'CloudProvider'")
	}
	if args.Region == nil {
		return nil, errors.New("invalid value for required argument 'Region'")
	}
	if args.TenantName == nil {
		return nil, errors.New("invalid value for required argument 'TenantName'")
	}
	if args.Topic == nil {
		return nil, errors.New("invalid value for required argument 'Topic'")
	}
	if args.UserEmail == nil {
		return nil, errors.New("invalid value for required argument 'UserEmail'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource StreamingTenant
	err := ctx.RegisterResource("astra:index/streamingTenant:StreamingTenant", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStreamingTenant gets an existing StreamingTenant resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStreamingTenant(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StreamingTenantState, opts ...pulumi.ResourceOption) (*StreamingTenant, error) {
	var resource StreamingTenant
	err := ctx.ReadResource("astra:index/streamingTenant:StreamingTenant", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StreamingTenant resources.
type streamingTenantState struct {
	// Cloud provider
	CloudProvider *string `pulumi:"cloudProvider"`
	// cloud region
	Region *string `pulumi:"region"`
	// Streaming tenant name.
	TenantName *string `pulumi:"tenantName"`
	// Streaming tenant topic.
	Topic *string `pulumi:"topic"`
	// User email for tenant.
	UserEmail *string `pulumi:"userEmail"`
}

type StreamingTenantState struct {
	// Cloud provider
	CloudProvider pulumi.StringPtrInput
	// cloud region
	Region pulumi.StringPtrInput
	// Streaming tenant name.
	TenantName pulumi.StringPtrInput
	// Streaming tenant topic.
	Topic pulumi.StringPtrInput
	// User email for tenant.
	UserEmail pulumi.StringPtrInput
}

func (StreamingTenantState) ElementType() reflect.Type {
	return reflect.TypeOf((*streamingTenantState)(nil)).Elem()
}

type streamingTenantArgs struct {
	// Cloud provider
	CloudProvider string `pulumi:"cloudProvider"`
	// cloud region
	Region string `pulumi:"region"`
	// Streaming tenant name.
	TenantName string `pulumi:"tenantName"`
	// Streaming tenant topic.
	Topic string `pulumi:"topic"`
	// User email for tenant.
	UserEmail string `pulumi:"userEmail"`
}

// The set of arguments for constructing a StreamingTenant resource.
type StreamingTenantArgs struct {
	// Cloud provider
	CloudProvider pulumi.StringInput
	// cloud region
	Region pulumi.StringInput
	// Streaming tenant name.
	TenantName pulumi.StringInput
	// Streaming tenant topic.
	Topic pulumi.StringInput
	// User email for tenant.
	UserEmail pulumi.StringInput
}

func (StreamingTenantArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*streamingTenantArgs)(nil)).Elem()
}

type StreamingTenantInput interface {
	pulumi.Input

	ToStreamingTenantOutput() StreamingTenantOutput
	ToStreamingTenantOutputWithContext(ctx context.Context) StreamingTenantOutput
}

func (*StreamingTenant) ElementType() reflect.Type {
	return reflect.TypeOf((**StreamingTenant)(nil)).Elem()
}

func (i *StreamingTenant) ToStreamingTenantOutput() StreamingTenantOutput {
	return i.ToStreamingTenantOutputWithContext(context.Background())
}

func (i *StreamingTenant) ToStreamingTenantOutputWithContext(ctx context.Context) StreamingTenantOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StreamingTenantOutput)
}

// StreamingTenantArrayInput is an input type that accepts StreamingTenantArray and StreamingTenantArrayOutput values.
// You can construct a concrete instance of `StreamingTenantArrayInput` via:
//
//          StreamingTenantArray{ StreamingTenantArgs{...} }
type StreamingTenantArrayInput interface {
	pulumi.Input

	ToStreamingTenantArrayOutput() StreamingTenantArrayOutput
	ToStreamingTenantArrayOutputWithContext(context.Context) StreamingTenantArrayOutput
}

type StreamingTenantArray []StreamingTenantInput

func (StreamingTenantArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*StreamingTenant)(nil)).Elem()
}

func (i StreamingTenantArray) ToStreamingTenantArrayOutput() StreamingTenantArrayOutput {
	return i.ToStreamingTenantArrayOutputWithContext(context.Background())
}

func (i StreamingTenantArray) ToStreamingTenantArrayOutputWithContext(ctx context.Context) StreamingTenantArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StreamingTenantArrayOutput)
}

// StreamingTenantMapInput is an input type that accepts StreamingTenantMap and StreamingTenantMapOutput values.
// You can construct a concrete instance of `StreamingTenantMapInput` via:
//
//          StreamingTenantMap{ "key": StreamingTenantArgs{...} }
type StreamingTenantMapInput interface {
	pulumi.Input

	ToStreamingTenantMapOutput() StreamingTenantMapOutput
	ToStreamingTenantMapOutputWithContext(context.Context) StreamingTenantMapOutput
}

type StreamingTenantMap map[string]StreamingTenantInput

func (StreamingTenantMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*StreamingTenant)(nil)).Elem()
}

func (i StreamingTenantMap) ToStreamingTenantMapOutput() StreamingTenantMapOutput {
	return i.ToStreamingTenantMapOutputWithContext(context.Background())
}

func (i StreamingTenantMap) ToStreamingTenantMapOutputWithContext(ctx context.Context) StreamingTenantMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StreamingTenantMapOutput)
}

type StreamingTenantOutput struct{ *pulumi.OutputState }

func (StreamingTenantOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StreamingTenant)(nil)).Elem()
}

func (o StreamingTenantOutput) ToStreamingTenantOutput() StreamingTenantOutput {
	return o
}

func (o StreamingTenantOutput) ToStreamingTenantOutputWithContext(ctx context.Context) StreamingTenantOutput {
	return o
}

// Cloud provider
func (o StreamingTenantOutput) CloudProvider() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamingTenant) pulumi.StringOutput { return v.CloudProvider }).(pulumi.StringOutput)
}

// cloud region
func (o StreamingTenantOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamingTenant) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// Streaming tenant name.
func (o StreamingTenantOutput) TenantName() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamingTenant) pulumi.StringOutput { return v.TenantName }).(pulumi.StringOutput)
}

// Streaming tenant topic.
func (o StreamingTenantOutput) Topic() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamingTenant) pulumi.StringOutput { return v.Topic }).(pulumi.StringOutput)
}

// User email for tenant.
func (o StreamingTenantOutput) UserEmail() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamingTenant) pulumi.StringOutput { return v.UserEmail }).(pulumi.StringOutput)
}

type StreamingTenantArrayOutput struct{ *pulumi.OutputState }

func (StreamingTenantArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*StreamingTenant)(nil)).Elem()
}

func (o StreamingTenantArrayOutput) ToStreamingTenantArrayOutput() StreamingTenantArrayOutput {
	return o
}

func (o StreamingTenantArrayOutput) ToStreamingTenantArrayOutputWithContext(ctx context.Context) StreamingTenantArrayOutput {
	return o
}

func (o StreamingTenantArrayOutput) Index(i pulumi.IntInput) StreamingTenantOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *StreamingTenant {
		return vs[0].([]*StreamingTenant)[vs[1].(int)]
	}).(StreamingTenantOutput)
}

type StreamingTenantMapOutput struct{ *pulumi.OutputState }

func (StreamingTenantMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*StreamingTenant)(nil)).Elem()
}

func (o StreamingTenantMapOutput) ToStreamingTenantMapOutput() StreamingTenantMapOutput {
	return o
}

func (o StreamingTenantMapOutput) ToStreamingTenantMapOutputWithContext(ctx context.Context) StreamingTenantMapOutput {
	return o
}

func (o StreamingTenantMapOutput) MapIndex(k pulumi.StringInput) StreamingTenantOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *StreamingTenant {
		return vs[0].(map[string]*StreamingTenant)[vs[1].(string)]
	}).(StreamingTenantOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StreamingTenantInput)(nil)).Elem(), &StreamingTenant{})
	pulumi.RegisterInputType(reflect.TypeOf((*StreamingTenantArrayInput)(nil)).Elem(), StreamingTenantArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*StreamingTenantMapInput)(nil)).Elem(), StreamingTenantMap{})
	pulumi.RegisterOutputType(StreamingTenantOutput{})
	pulumi.RegisterOutputType(StreamingTenantArrayOutput{})
	pulumi.RegisterOutputType(StreamingTenantMapOutput{})
}
