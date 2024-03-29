// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package astra

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// `PrivateLinkEndpoint` completes the creation of a private link endpoint by associating it with your endpoint.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/ec2"
// 	"github.com/pulumi/pulumi-azure/sdk/v4/go/azure/core"
// 	"github.com/pulumi/pulumi-azure/sdk/v4/go/azure/network"
// 	"github.com/pulumi/pulumi-azure/sdk/v4/go/azure/privatelink"
// 	"github.com/pulumi/pulumi-gcp/sdk/v5/go/gcp/compute"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/pulumiverse/pulumi-astra/sdk/go/astra"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := astra.NewPrivateLink(ctx, "exampleAstraIndex/privateLinkPrivateLink", &astra.PrivateLinkArgs{
// 			AllowedPrincipals: pulumi.StringArray{
// 				pulumi.String("arn:aws:iam::445559476293:user/Sebastian"),
// 			},
// 			DatabaseId:   pulumi.String("a6bc9c26-e7ce-424f-84c7-0a00afb12588"),
// 			DatacenterId: pulumi.String("a6bc9c26-e7ce-424f-84c7-0a00afb12588-1"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleVpcEndpoint, err := ec2.NewVpcEndpoint(ctx, "exampleVpcEndpoint", &ec2.VpcEndpointArgs{
// 			VpcId:           pulumi.String("vpc-f939e884"),
// 			ServiceName:     exampleAstraIndex / privateLinkPrivateLink.ServiceName,
// 			VpcEndpointType: pulumi.String("Interface"),
// 			SubnetIds: pulumi.StringArray{
// 				pulumi.String("subnet-4d376300"),
// 				pulumi.String("subnet-4d85066c"),
// 				pulumi.String("subnet-030e8b65"),
// 			},
// 			SecurityGroupIds: pulumi.StringArray{
// 				pulumi.String("sg-74ae4d41"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = astra.NewPrivateLinkEndpoint(ctx, "examplePrivateLinkEndpoint", &astra.PrivateLinkEndpointArgs{
// 			DatabaseId:   pulumi.String("a6bc9c26-e7ce-424f-84c7-0a00afb12588"),
// 			DatacenterId: pulumi.String("a6bc9c26-e7ce-424f-84c7-0a00afb12588-1"),
// 			EndpointId:   exampleVpcEndpoint.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = astra.NewPrivateLink(ctx, "examplePrivateLink", &astra.PrivateLinkArgs{
// 			AllowedPrincipals: pulumi.StringArray{
// 				pulumi.String("my-project"),
// 			},
// 			DatabaseId:   pulumi.String("a6bc9c26-e7ce-424f-84c7-0a00afb12588"),
// 			DatacenterId: pulumi.String("a6bc9c26-e7ce-424f-84c7-0a00afb12588-1"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleNetwork, err := compute.NewNetwork(ctx, "exampleNetwork", &compute.NetworkArgs{
// 			AutoCreateSubnetworks: pulumi.Bool(false),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleSubnetwork, err := compute.NewSubnetwork(ctx, "exampleSubnetwork", &compute.SubnetworkArgs{
// 			IpCidrRange: pulumi.String("10.142.0.0/20"),
// 			Region:      pulumi.String("us-east1"),
// 			Network:     exampleNetwork.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleAddress, err := compute.NewAddress(ctx, "exampleAddress", &compute.AddressArgs{
// 			Subnetwork:  exampleSubnetwork.ID(),
// 			AddressType: pulumi.String("INTERNAL"),
// 			Region:      pulumi.String("us-east1"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = compute.NewForwardingRule(ctx, "exampleForwardingRule", &compute.ForwardingRuleArgs{
// 			Target:              pulumi.String(fmt.Sprintf("https://www.googleapis.com/compute/v1/%v", exampleAstraIndex/privateLinkPrivateLink.ServiceName)),
// 			Project:             exampleNetwork.Project,
// 			IpAddress:           exampleAddress.ID(),
// 			Network:             exampleNetwork.ID(),
// 			Region:              pulumi.String("us-east1"),
// 			LoadBalancingScheme: pulumi.String(""),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = astra.NewPrivateLinkEndpoint(ctx, "endpoint", &astra.PrivateLinkEndpointArgs{
// 			DatabaseId:   pulumi.String("a6bc9c26-e7ce-424f-84c7-0a00afb12588"),
// 			DatacenterId: pulumi.String("a6bc9c26-e7ce-424f-84c7-0a00afb12588-1"),
// 			EndpointId:   pulumi.String("13585698993864708"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		current, err := core.LookupSubscription(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		exampleResourceGroup, err := core.LookupResourceGroup(ctx, &core.LookupResourceGroupArgs{
// 			Name: "example-rg",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		exampleVirtualNetwork, err := network.LookupVirtualNetwork(ctx, &network.LookupVirtualNetworkArgs{
// 			Name:              "example-virtual-network",
// 			ResourceGroupName: exampleResourceGroup.Name,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		exampleSubnet, err := network.LookupSubnet(ctx, &network.LookupSubnetArgs{
// 			Name:               "example-subnet",
// 			VirtualNetworkName: exampleVirtualNetwork.Name,
// 			ResourceGroupName:  exampleResourceGroup.Name,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = astra.NewPrivateLink(ctx, "exampleIndex/privateLinkPrivateLink", &astra.PrivateLinkArgs{
// 			AllowedPrincipals: pulumi.StringArray{
// 				pulumi.String(current.SubscriptionId),
// 			},
// 			DatabaseId:   pulumi.String("a6bc9c26-e7ce-424f-84c7-0a00afb12588"),
// 			DatacenterId: pulumi.String("a6bc9c26-e7ce-424f-84c7-0a00afb12588-1"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleEndpoint, err := privatelink.NewEndpoint(ctx, "exampleEndpoint", &privatelink.EndpointArgs{
// 			Location:          pulumi.String(exampleResourceGroup.Location),
// 			ResourceGroupName: pulumi.String(exampleResourceGroup.Name),
// 			SubnetId:          pulumi.String(exampleSubnet.Id),
// 			PrivateServiceConnection: &privatelink.EndpointPrivateServiceConnectionArgs{
// 				Name:                           pulumi.String("example-private-connection"),
// 				PrivateConnectionResourceAlias: exampleAstraIndex / privateLinkPrivateLink.ServiceName,
// 				IsManualConnection:             pulumi.Bool(true),
// 				RequestMessage:                 pulumi.String("Private connection from AKS subnet to Astra DB"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = astra.NewPrivateLinkEndpoint(ctx, "azPrivateLinkEndpoint", &astra.PrivateLinkEndpointArgs{
// 			DatabaseId:   pulumi.String("a6bc9c26-e7ce-424f-84c7-0a00afb12588"),
// 			DatacenterId: pulumi.String("a6bc9c26-e7ce-424f-84c7-0a00afb12588-1"),
// 			EndpointId: exampleEndpoint.Name.ApplyT(func(name string) (string, error) {
// 				return fmt.Sprintf("%v/providers/Microsoft.Network/privateEndpoints/%v", exampleResourceGroup.Id, name), nil
// 			}).(pulumi.StringOutput),
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
// # Amazon AWS example
//
// ```sh
//  $ pulumi import astra:index/privateLinkEndpoint:PrivateLinkEndpoint example a6bc9c26-e7ce-424f-84c7-0a00afb12588/datacenter/a6bc9c26-e7ce-424f-84c7-0a00afb12588-1/endpoint/vpce-0f7aed6e7a18a1791
// ```
//
// # Google GCP example
//
// ```sh
//  $ pulumi import astra:index/privateLinkEndpoint:PrivateLinkEndpoint example a6bc9c26-e7ce-424f-84c7-0a00afb12588/datacenter/a6bc9c26-e7ce-424f-84c7-0a00afb12588-1/endpoint/13585698993864708
// ```
//
// # Azure EKS example
//
// ```sh
//  $ pulumi import astra:index/privateLinkEndpoint:PrivateLinkEndpoint example a6bc9c26-e7ce-424f-84c7-0a00afb12588/datacenter/a6bc9c26-e7ce-424f-84c7-0a00afb12588-1/endpoint/dc5ee5b1-4fc2-463e-a56b-ff54dd38b879/providers/Microsoft.Network/privateEndpoints/private-endpoint-example
// ```
type PrivateLinkEndpoint struct {
	pulumi.CustomResourceState

	// Endpoint ID for referencing within Astra. May be different than the endpointId of this resource.
	AstraEndpointId pulumi.StringOutput `pulumi:"astraEndpointId"`
	// The ID of the Astra database.
	DatabaseId pulumi.StringOutput `pulumi:"databaseId"`
	// Astra datacenter in the region where the private link will be created.
	DatacenterId pulumi.StringOutput `pulumi:"datacenterId"`
	// Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
	EndpointId pulumi.StringOutput `pulumi:"endpointId"`
}

// NewPrivateLinkEndpoint registers a new resource with the given unique name, arguments, and options.
func NewPrivateLinkEndpoint(ctx *pulumi.Context,
	name string, args *PrivateLinkEndpointArgs, opts ...pulumi.ResourceOption) (*PrivateLinkEndpoint, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DatabaseId == nil {
		return nil, errors.New("invalid value for required argument 'DatabaseId'")
	}
	if args.DatacenterId == nil {
		return nil, errors.New("invalid value for required argument 'DatacenterId'")
	}
	if args.EndpointId == nil {
		return nil, errors.New("invalid value for required argument 'EndpointId'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource PrivateLinkEndpoint
	err := ctx.RegisterResource("astra:index/privateLinkEndpoint:PrivateLinkEndpoint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPrivateLinkEndpoint gets an existing PrivateLinkEndpoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPrivateLinkEndpoint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PrivateLinkEndpointState, opts ...pulumi.ResourceOption) (*PrivateLinkEndpoint, error) {
	var resource PrivateLinkEndpoint
	err := ctx.ReadResource("astra:index/privateLinkEndpoint:PrivateLinkEndpoint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PrivateLinkEndpoint resources.
type privateLinkEndpointState struct {
	// Endpoint ID for referencing within Astra. May be different than the endpointId of this resource.
	AstraEndpointId *string `pulumi:"astraEndpointId"`
	// The ID of the Astra database.
	DatabaseId *string `pulumi:"databaseId"`
	// Astra datacenter in the region where the private link will be created.
	DatacenterId *string `pulumi:"datacenterId"`
	// Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
	EndpointId *string `pulumi:"endpointId"`
}

type PrivateLinkEndpointState struct {
	// Endpoint ID for referencing within Astra. May be different than the endpointId of this resource.
	AstraEndpointId pulumi.StringPtrInput
	// The ID of the Astra database.
	DatabaseId pulumi.StringPtrInput
	// Astra datacenter in the region where the private link will be created.
	DatacenterId pulumi.StringPtrInput
	// Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
	EndpointId pulumi.StringPtrInput
}

func (PrivateLinkEndpointState) ElementType() reflect.Type {
	return reflect.TypeOf((*privateLinkEndpointState)(nil)).Elem()
}

type privateLinkEndpointArgs struct {
	// The ID of the Astra database.
	DatabaseId string `pulumi:"databaseId"`
	// Astra datacenter in the region where the private link will be created.
	DatacenterId string `pulumi:"datacenterId"`
	// Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
	EndpointId string `pulumi:"endpointId"`
}

// The set of arguments for constructing a PrivateLinkEndpoint resource.
type PrivateLinkEndpointArgs struct {
	// The ID of the Astra database.
	DatabaseId pulumi.StringInput
	// Astra datacenter in the region where the private link will be created.
	DatacenterId pulumi.StringInput
	// Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
	EndpointId pulumi.StringInput
}

func (PrivateLinkEndpointArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*privateLinkEndpointArgs)(nil)).Elem()
}

type PrivateLinkEndpointInput interface {
	pulumi.Input

	ToPrivateLinkEndpointOutput() PrivateLinkEndpointOutput
	ToPrivateLinkEndpointOutputWithContext(ctx context.Context) PrivateLinkEndpointOutput
}

func (*PrivateLinkEndpoint) ElementType() reflect.Type {
	return reflect.TypeOf((**PrivateLinkEndpoint)(nil)).Elem()
}

func (i *PrivateLinkEndpoint) ToPrivateLinkEndpointOutput() PrivateLinkEndpointOutput {
	return i.ToPrivateLinkEndpointOutputWithContext(context.Background())
}

func (i *PrivateLinkEndpoint) ToPrivateLinkEndpointOutputWithContext(ctx context.Context) PrivateLinkEndpointOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PrivateLinkEndpointOutput)
}

// PrivateLinkEndpointArrayInput is an input type that accepts PrivateLinkEndpointArray and PrivateLinkEndpointArrayOutput values.
// You can construct a concrete instance of `PrivateLinkEndpointArrayInput` via:
//
//          PrivateLinkEndpointArray{ PrivateLinkEndpointArgs{...} }
type PrivateLinkEndpointArrayInput interface {
	pulumi.Input

	ToPrivateLinkEndpointArrayOutput() PrivateLinkEndpointArrayOutput
	ToPrivateLinkEndpointArrayOutputWithContext(context.Context) PrivateLinkEndpointArrayOutput
}

type PrivateLinkEndpointArray []PrivateLinkEndpointInput

func (PrivateLinkEndpointArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PrivateLinkEndpoint)(nil)).Elem()
}

func (i PrivateLinkEndpointArray) ToPrivateLinkEndpointArrayOutput() PrivateLinkEndpointArrayOutput {
	return i.ToPrivateLinkEndpointArrayOutputWithContext(context.Background())
}

func (i PrivateLinkEndpointArray) ToPrivateLinkEndpointArrayOutputWithContext(ctx context.Context) PrivateLinkEndpointArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PrivateLinkEndpointArrayOutput)
}

// PrivateLinkEndpointMapInput is an input type that accepts PrivateLinkEndpointMap and PrivateLinkEndpointMapOutput values.
// You can construct a concrete instance of `PrivateLinkEndpointMapInput` via:
//
//          PrivateLinkEndpointMap{ "key": PrivateLinkEndpointArgs{...} }
type PrivateLinkEndpointMapInput interface {
	pulumi.Input

	ToPrivateLinkEndpointMapOutput() PrivateLinkEndpointMapOutput
	ToPrivateLinkEndpointMapOutputWithContext(context.Context) PrivateLinkEndpointMapOutput
}

type PrivateLinkEndpointMap map[string]PrivateLinkEndpointInput

func (PrivateLinkEndpointMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PrivateLinkEndpoint)(nil)).Elem()
}

func (i PrivateLinkEndpointMap) ToPrivateLinkEndpointMapOutput() PrivateLinkEndpointMapOutput {
	return i.ToPrivateLinkEndpointMapOutputWithContext(context.Background())
}

func (i PrivateLinkEndpointMap) ToPrivateLinkEndpointMapOutputWithContext(ctx context.Context) PrivateLinkEndpointMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PrivateLinkEndpointMapOutput)
}

type PrivateLinkEndpointOutput struct{ *pulumi.OutputState }

func (PrivateLinkEndpointOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PrivateLinkEndpoint)(nil)).Elem()
}

func (o PrivateLinkEndpointOutput) ToPrivateLinkEndpointOutput() PrivateLinkEndpointOutput {
	return o
}

func (o PrivateLinkEndpointOutput) ToPrivateLinkEndpointOutputWithContext(ctx context.Context) PrivateLinkEndpointOutput {
	return o
}

// Endpoint ID for referencing within Astra. May be different than the endpointId of this resource.
func (o PrivateLinkEndpointOutput) AstraEndpointId() pulumi.StringOutput {
	return o.ApplyT(func(v *PrivateLinkEndpoint) pulumi.StringOutput { return v.AstraEndpointId }).(pulumi.StringOutput)
}

// The ID of the Astra database.
func (o PrivateLinkEndpointOutput) DatabaseId() pulumi.StringOutput {
	return o.ApplyT(func(v *PrivateLinkEndpoint) pulumi.StringOutput { return v.DatabaseId }).(pulumi.StringOutput)
}

// Astra datacenter in the region where the private link will be created.
func (o PrivateLinkEndpointOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v *PrivateLinkEndpoint) pulumi.StringOutput { return v.DatacenterId }).(pulumi.StringOutput)
}

// Endpoint created in your cloud provider account example: "vpce-svc-1148ea04af8675309"
func (o PrivateLinkEndpointOutput) EndpointId() pulumi.StringOutput {
	return o.ApplyT(func(v *PrivateLinkEndpoint) pulumi.StringOutput { return v.EndpointId }).(pulumi.StringOutput)
}

type PrivateLinkEndpointArrayOutput struct{ *pulumi.OutputState }

func (PrivateLinkEndpointArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PrivateLinkEndpoint)(nil)).Elem()
}

func (o PrivateLinkEndpointArrayOutput) ToPrivateLinkEndpointArrayOutput() PrivateLinkEndpointArrayOutput {
	return o
}

func (o PrivateLinkEndpointArrayOutput) ToPrivateLinkEndpointArrayOutputWithContext(ctx context.Context) PrivateLinkEndpointArrayOutput {
	return o
}

func (o PrivateLinkEndpointArrayOutput) Index(i pulumi.IntInput) PrivateLinkEndpointOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *PrivateLinkEndpoint {
		return vs[0].([]*PrivateLinkEndpoint)[vs[1].(int)]
	}).(PrivateLinkEndpointOutput)
}

type PrivateLinkEndpointMapOutput struct{ *pulumi.OutputState }

func (PrivateLinkEndpointMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PrivateLinkEndpoint)(nil)).Elem()
}

func (o PrivateLinkEndpointMapOutput) ToPrivateLinkEndpointMapOutput() PrivateLinkEndpointMapOutput {
	return o
}

func (o PrivateLinkEndpointMapOutput) ToPrivateLinkEndpointMapOutputWithContext(ctx context.Context) PrivateLinkEndpointMapOutput {
	return o
}

func (o PrivateLinkEndpointMapOutput) MapIndex(k pulumi.StringInput) PrivateLinkEndpointOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *PrivateLinkEndpoint {
		return vs[0].(map[string]*PrivateLinkEndpoint)[vs[1].(string)]
	}).(PrivateLinkEndpointOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PrivateLinkEndpointInput)(nil)).Elem(), &PrivateLinkEndpoint{})
	pulumi.RegisterInputType(reflect.TypeOf((*PrivateLinkEndpointArrayInput)(nil)).Elem(), PrivateLinkEndpointArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PrivateLinkEndpointMapInput)(nil)).Elem(), PrivateLinkEndpointMap{})
	pulumi.RegisterOutputType(PrivateLinkEndpointOutput{})
	pulumi.RegisterOutputType(PrivateLinkEndpointArrayOutput{})
	pulumi.RegisterOutputType(PrivateLinkEndpointMapOutput{})
}
