// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package astra

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// `Token` resource represents a token with a specific role assigned.
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
// 		_, err := astra.NewToken(ctx, "example", &astra.TokenArgs{
// 			Roles: pulumi.StringArray{
// 				pulumi.String("a8cd363d-5069-4a2b-86d8-0578139812ac"),
// 			},
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
//  $ pulumi import astra:index/token:Token example client-secret
// ```
type Token struct {
	pulumi.CustomResourceState

	// Client id, use as username in cql to connect
	ClientId pulumi.StringOutput `pulumi:"clientId"`
	// List of Role IDs to be assigned to the generated token
	Roles pulumi.StringArrayOutput `pulumi:"roles"`
	// Secret, use as password in cql to connect
	Secret pulumi.StringOutput `pulumi:"secret"`
	// Token, use as auth bearer for API calls or as password in combination with the word `token` in cql
	Token pulumi.StringOutput `pulumi:"token"`
}

// NewToken registers a new resource with the given unique name, arguments, and options.
func NewToken(ctx *pulumi.Context,
	name string, args *TokenArgs, opts ...pulumi.ResourceOption) (*Token, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Roles == nil {
		return nil, errors.New("invalid value for required argument 'Roles'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource Token
	err := ctx.RegisterResource("astra:index/token:Token", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetToken gets an existing Token resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetToken(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TokenState, opts ...pulumi.ResourceOption) (*Token, error) {
	var resource Token
	err := ctx.ReadResource("astra:index/token:Token", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Token resources.
type tokenState struct {
	// Client id, use as username in cql to connect
	ClientId *string `pulumi:"clientId"`
	// List of Role IDs to be assigned to the generated token
	Roles []string `pulumi:"roles"`
	// Secret, use as password in cql to connect
	Secret *string `pulumi:"secret"`
	// Token, use as auth bearer for API calls or as password in combination with the word `token` in cql
	Token *string `pulumi:"token"`
}

type TokenState struct {
	// Client id, use as username in cql to connect
	ClientId pulumi.StringPtrInput
	// List of Role IDs to be assigned to the generated token
	Roles pulumi.StringArrayInput
	// Secret, use as password in cql to connect
	Secret pulumi.StringPtrInput
	// Token, use as auth bearer for API calls or as password in combination with the word `token` in cql
	Token pulumi.StringPtrInput
}

func (TokenState) ElementType() reflect.Type {
	return reflect.TypeOf((*tokenState)(nil)).Elem()
}

type tokenArgs struct {
	// List of Role IDs to be assigned to the generated token
	Roles []string `pulumi:"roles"`
}

// The set of arguments for constructing a Token resource.
type TokenArgs struct {
	// List of Role IDs to be assigned to the generated token
	Roles pulumi.StringArrayInput
}

func (TokenArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tokenArgs)(nil)).Elem()
}

type TokenInput interface {
	pulumi.Input

	ToTokenOutput() TokenOutput
	ToTokenOutputWithContext(ctx context.Context) TokenOutput
}

func (*Token) ElementType() reflect.Type {
	return reflect.TypeOf((**Token)(nil)).Elem()
}

func (i *Token) ToTokenOutput() TokenOutput {
	return i.ToTokenOutputWithContext(context.Background())
}

func (i *Token) ToTokenOutputWithContext(ctx context.Context) TokenOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TokenOutput)
}

// TokenArrayInput is an input type that accepts TokenArray and TokenArrayOutput values.
// You can construct a concrete instance of `TokenArrayInput` via:
//
//          TokenArray{ TokenArgs{...} }
type TokenArrayInput interface {
	pulumi.Input

	ToTokenArrayOutput() TokenArrayOutput
	ToTokenArrayOutputWithContext(context.Context) TokenArrayOutput
}

type TokenArray []TokenInput

func (TokenArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Token)(nil)).Elem()
}

func (i TokenArray) ToTokenArrayOutput() TokenArrayOutput {
	return i.ToTokenArrayOutputWithContext(context.Background())
}

func (i TokenArray) ToTokenArrayOutputWithContext(ctx context.Context) TokenArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TokenArrayOutput)
}

// TokenMapInput is an input type that accepts TokenMap and TokenMapOutput values.
// You can construct a concrete instance of `TokenMapInput` via:
//
//          TokenMap{ "key": TokenArgs{...} }
type TokenMapInput interface {
	pulumi.Input

	ToTokenMapOutput() TokenMapOutput
	ToTokenMapOutputWithContext(context.Context) TokenMapOutput
}

type TokenMap map[string]TokenInput

func (TokenMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Token)(nil)).Elem()
}

func (i TokenMap) ToTokenMapOutput() TokenMapOutput {
	return i.ToTokenMapOutputWithContext(context.Background())
}

func (i TokenMap) ToTokenMapOutputWithContext(ctx context.Context) TokenMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TokenMapOutput)
}

type TokenOutput struct{ *pulumi.OutputState }

func (TokenOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Token)(nil)).Elem()
}

func (o TokenOutput) ToTokenOutput() TokenOutput {
	return o
}

func (o TokenOutput) ToTokenOutputWithContext(ctx context.Context) TokenOutput {
	return o
}

// Client id, use as username in cql to connect
func (o TokenOutput) ClientId() pulumi.StringOutput {
	return o.ApplyT(func(v *Token) pulumi.StringOutput { return v.ClientId }).(pulumi.StringOutput)
}

// List of Role IDs to be assigned to the generated token
func (o TokenOutput) Roles() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Token) pulumi.StringArrayOutput { return v.Roles }).(pulumi.StringArrayOutput)
}

// Secret, use as password in cql to connect
func (o TokenOutput) Secret() pulumi.StringOutput {
	return o.ApplyT(func(v *Token) pulumi.StringOutput { return v.Secret }).(pulumi.StringOutput)
}

// Token, use as auth bearer for API calls or as password in combination with the word `token` in cql
func (o TokenOutput) Token() pulumi.StringOutput {
	return o.ApplyT(func(v *Token) pulumi.StringOutput { return v.Token }).(pulumi.StringOutput)
}

type TokenArrayOutput struct{ *pulumi.OutputState }

func (TokenArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Token)(nil)).Elem()
}

func (o TokenArrayOutput) ToTokenArrayOutput() TokenArrayOutput {
	return o
}

func (o TokenArrayOutput) ToTokenArrayOutputWithContext(ctx context.Context) TokenArrayOutput {
	return o
}

func (o TokenArrayOutput) Index(i pulumi.IntInput) TokenOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Token {
		return vs[0].([]*Token)[vs[1].(int)]
	}).(TokenOutput)
}

type TokenMapOutput struct{ *pulumi.OutputState }

func (TokenMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Token)(nil)).Elem()
}

func (o TokenMapOutput) ToTokenMapOutput() TokenMapOutput {
	return o
}

func (o TokenMapOutput) ToTokenMapOutputWithContext(ctx context.Context) TokenMapOutput {
	return o
}

func (o TokenMapOutput) MapIndex(k pulumi.StringInput) TokenOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Token {
		return vs[0].(map[string]*Token)[vs[1].(string)]
	}).(TokenOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TokenInput)(nil)).Elem(), &Token{})
	pulumi.RegisterInputType(reflect.TypeOf((*TokenArrayInput)(nil)).Elem(), TokenArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TokenMapInput)(nil)).Elem(), TokenMap{})
	pulumi.RegisterOutputType(TokenOutput{})
	pulumi.RegisterOutputType(TokenArrayOutput{})
	pulumi.RegisterOutputType(TokenMapOutput{})
}
