// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package index

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// `Keyspace` provides a keyspace resource. Keyspaces are groupings of tables for Cassandra. `Keyspace` resources are associated with a database id. You can have multiple keyspaces per DB in addition to the default keyspace provided in the `Database` resource.
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
// 		_, err := astra.NewKeyspace(ctx, "example", &astra.KeyspaceArgs{
// 			DatabaseId: pulumi.String("48bfc13b-c1a5-48db-b70f-b6ef9709872b"),
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
// # the import id includes the database_id and the keyspace name.
//
// ```sh
//  $ pulumi import astra:index/keyspace:Keyspace example 48bfc13b-c1a5-48db-b70f-b6ef9709872b/keyspace/example
// ```
type Keyspace struct {
	pulumi.CustomResourceState

	// Astra database to create the keyspace.
	DatabaseId pulumi.StringOutput `pulumi:"databaseId"`
	// Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
	// as the first character.
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewKeyspace registers a new resource with the given unique name, arguments, and options.
func NewKeyspace(ctx *pulumi.Context,
	name string, args *KeyspaceArgs, opts ...pulumi.ResourceOption) (*Keyspace, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DatabaseId == nil {
		return nil, errors.New("invalid value for required argument 'DatabaseId'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource Keyspace
	err := ctx.RegisterResource("astra:index/keyspace:Keyspace", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetKeyspace gets an existing Keyspace resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetKeyspace(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *KeyspaceState, opts ...pulumi.ResourceOption) (*Keyspace, error) {
	var resource Keyspace
	err := ctx.ReadResource("astra:index/keyspace:Keyspace", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Keyspace resources.
type keyspaceState struct {
	// Astra database to create the keyspace.
	DatabaseId *string `pulumi:"databaseId"`
	// Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
	// as the first character.
	Name *string `pulumi:"name"`
}

type KeyspaceState struct {
	// Astra database to create the keyspace.
	DatabaseId pulumi.StringPtrInput
	// Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
	// as the first character.
	Name pulumi.StringPtrInput
}

func (KeyspaceState) ElementType() reflect.Type {
	return reflect.TypeOf((*keyspaceState)(nil)).Elem()
}

type keyspaceArgs struct {
	// Astra database to create the keyspace.
	DatabaseId string `pulumi:"databaseId"`
	// Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
	// as the first character.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a Keyspace resource.
type KeyspaceArgs struct {
	// Astra database to create the keyspace.
	DatabaseId pulumi.StringInput
	// Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
	// as the first character.
	Name pulumi.StringPtrInput
}

func (KeyspaceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*keyspaceArgs)(nil)).Elem()
}

type KeyspaceInput interface {
	pulumi.Input

	ToKeyspaceOutput() KeyspaceOutput
	ToKeyspaceOutputWithContext(ctx context.Context) KeyspaceOutput
}

func (*Keyspace) ElementType() reflect.Type {
	return reflect.TypeOf((**Keyspace)(nil)).Elem()
}

func (i *Keyspace) ToKeyspaceOutput() KeyspaceOutput {
	return i.ToKeyspaceOutputWithContext(context.Background())
}

func (i *Keyspace) ToKeyspaceOutputWithContext(ctx context.Context) KeyspaceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KeyspaceOutput)
}

// KeyspaceArrayInput is an input type that accepts KeyspaceArray and KeyspaceArrayOutput values.
// You can construct a concrete instance of `KeyspaceArrayInput` via:
//
//          KeyspaceArray{ KeyspaceArgs{...} }
type KeyspaceArrayInput interface {
	pulumi.Input

	ToKeyspaceArrayOutput() KeyspaceArrayOutput
	ToKeyspaceArrayOutputWithContext(context.Context) KeyspaceArrayOutput
}

type KeyspaceArray []KeyspaceInput

func (KeyspaceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Keyspace)(nil)).Elem()
}

func (i KeyspaceArray) ToKeyspaceArrayOutput() KeyspaceArrayOutput {
	return i.ToKeyspaceArrayOutputWithContext(context.Background())
}

func (i KeyspaceArray) ToKeyspaceArrayOutputWithContext(ctx context.Context) KeyspaceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KeyspaceArrayOutput)
}

// KeyspaceMapInput is an input type that accepts KeyspaceMap and KeyspaceMapOutput values.
// You can construct a concrete instance of `KeyspaceMapInput` via:
//
//          KeyspaceMap{ "key": KeyspaceArgs{...} }
type KeyspaceMapInput interface {
	pulumi.Input

	ToKeyspaceMapOutput() KeyspaceMapOutput
	ToKeyspaceMapOutputWithContext(context.Context) KeyspaceMapOutput
}

type KeyspaceMap map[string]KeyspaceInput

func (KeyspaceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Keyspace)(nil)).Elem()
}

func (i KeyspaceMap) ToKeyspaceMapOutput() KeyspaceMapOutput {
	return i.ToKeyspaceMapOutputWithContext(context.Background())
}

func (i KeyspaceMap) ToKeyspaceMapOutputWithContext(ctx context.Context) KeyspaceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KeyspaceMapOutput)
}

type KeyspaceOutput struct{ *pulumi.OutputState }

func (KeyspaceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Keyspace)(nil)).Elem()
}

func (o KeyspaceOutput) ToKeyspaceOutput() KeyspaceOutput {
	return o
}

func (o KeyspaceOutput) ToKeyspaceOutputWithContext(ctx context.Context) KeyspaceOutput {
	return o
}

// Astra database to create the keyspace.
func (o KeyspaceOutput) DatabaseId() pulumi.StringOutput {
	return o.ApplyT(func(v *Keyspace) pulumi.StringOutput { return v.DatabaseId }).(pulumi.StringOutput)
}

// Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
// as the first character.
func (o KeyspaceOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Keyspace) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

type KeyspaceArrayOutput struct{ *pulumi.OutputState }

func (KeyspaceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Keyspace)(nil)).Elem()
}

func (o KeyspaceArrayOutput) ToKeyspaceArrayOutput() KeyspaceArrayOutput {
	return o
}

func (o KeyspaceArrayOutput) ToKeyspaceArrayOutputWithContext(ctx context.Context) KeyspaceArrayOutput {
	return o
}

func (o KeyspaceArrayOutput) Index(i pulumi.IntInput) KeyspaceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Keyspace {
		return vs[0].([]*Keyspace)[vs[1].(int)]
	}).(KeyspaceOutput)
}

type KeyspaceMapOutput struct{ *pulumi.OutputState }

func (KeyspaceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Keyspace)(nil)).Elem()
}

func (o KeyspaceMapOutput) ToKeyspaceMapOutput() KeyspaceMapOutput {
	return o
}

func (o KeyspaceMapOutput) ToKeyspaceMapOutputWithContext(ctx context.Context) KeyspaceMapOutput {
	return o
}

func (o KeyspaceMapOutput) MapIndex(k pulumi.StringInput) KeyspaceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Keyspace {
		return vs[0].(map[string]*Keyspace)[vs[1].(string)]
	}).(KeyspaceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*KeyspaceInput)(nil)).Elem(), &Keyspace{})
	pulumi.RegisterInputType(reflect.TypeOf((*KeyspaceArrayInput)(nil)).Elem(), KeyspaceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*KeyspaceMapInput)(nil)).Elem(), KeyspaceMap{})
	pulumi.RegisterOutputType(KeyspaceOutput{})
	pulumi.RegisterOutputType(KeyspaceArrayOutput{})
	pulumi.RegisterOutputType(KeyspaceMapOutput{})
}
