// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package astra

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// `Database` provides a datasource for Astra an Astra database. This can be used to select an existing database within your Astra Organization.
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
// 		_, err := astra.GetAstraDatabase(ctx, &GetAstraDatabaseArgs{
// 			DatabaseId: "8d356587-73b3-430a-9c0e-d780332e2afb",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetAstraDatabase(ctx *pulumi.Context, args *GetAstraDatabaseArgs, opts ...pulumi.InvokeOption) (*GetAstraDatabaseResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv GetAstraDatabaseResult
	err := ctx.Invoke("astra:index/getAstraDatabase:getAstraDatabase", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAstraDatabase.
type GetAstraDatabaseArgs struct {
	// Astra Database ID (system generated)
	DatabaseId string `pulumi:"databaseId"`
}

// A collection of values returned by getAstraDatabase.
type GetAstraDatabaseResult struct {
	// Additional keyspaces
	AdditionalKeyspaces []string `pulumi:"additionalKeyspaces"`
	// Cloud provider (AWS, GCP, AZURE)
	CloudProvider string `pulumi:"cloudProvider"`
	// URL for cqlsh web
	CqlshUrl string `pulumi:"cqlshUrl"`
	// REST API URL
	DataEndpointUrl string `pulumi:"dataEndpointUrl"`
	// Astra Database ID (system generated)
	DatabaseId string `pulumi:"databaseId"`
	// Map of Datacenter IDs. The map key is "cloud_provider.region". Example: "GCP.us-east4".
	Datacenters map[string]string `pulumi:"datacenters"`
	// URL for the grafana dashboard for this database
	GrafanaUrl string `pulumi:"grafanaUrl"`
	// Graphql URL
	GraphqlUrl string `pulumi:"graphqlUrl"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Initial keyspace
	Keyspace string `pulumi:"keyspace"`
	// Database name (user provided)
	Name string `pulumi:"name"`
	// Node count (not relevant for serverless databases)
	NodeCount int `pulumi:"nodeCount"`
	// Ordg id (system generated)
	OrganizationId string `pulumi:"organizationId"`
	// Owner id (system generated)
	OwnerId string `pulumi:"ownerId"`
	// Cloud provider region. Get list of supported regions from regions data-source
	Regions []string `pulumi:"regions"`
	// Replication Factor (not relevant for serverless databases)
	ReplicationFactor int `pulumi:"replicationFactor"`
	// Database status
	Status string `pulumi:"status"`
	// Storage Capacity (not relevant for serverelss databases)
	TotalStorage int `pulumi:"totalStorage"`
}

func GetAstraDatabaseOutput(ctx *pulumi.Context, args GetAstraDatabaseOutputArgs, opts ...pulumi.InvokeOption) GetAstraDatabaseResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetAstraDatabaseResult, error) {
			args := v.(GetAstraDatabaseArgs)
			r, err := GetAstraDatabase(ctx, &args, opts...)
			var s GetAstraDatabaseResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetAstraDatabaseResultOutput)
}

// A collection of arguments for invoking getAstraDatabase.
type GetAstraDatabaseOutputArgs struct {
	// Astra Database ID (system generated)
	DatabaseId pulumi.StringInput `pulumi:"databaseId"`
}

func (GetAstraDatabaseOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAstraDatabaseArgs)(nil)).Elem()
}

// A collection of values returned by getAstraDatabase.
type GetAstraDatabaseResultOutput struct{ *pulumi.OutputState }

func (GetAstraDatabaseResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAstraDatabaseResult)(nil)).Elem()
}

func (o GetAstraDatabaseResultOutput) ToGetAstraDatabaseResultOutput() GetAstraDatabaseResultOutput {
	return o
}

func (o GetAstraDatabaseResultOutput) ToGetAstraDatabaseResultOutputWithContext(ctx context.Context) GetAstraDatabaseResultOutput {
	return o
}

// Additional keyspaces
func (o GetAstraDatabaseResultOutput) AdditionalKeyspaces() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) []string { return v.AdditionalKeyspaces }).(pulumi.StringArrayOutput)
}

// Cloud provider (AWS, GCP, AZURE)
func (o GetAstraDatabaseResultOutput) CloudProvider() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.CloudProvider }).(pulumi.StringOutput)
}

// URL for cqlsh web
func (o GetAstraDatabaseResultOutput) CqlshUrl() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.CqlshUrl }).(pulumi.StringOutput)
}

// REST API URL
func (o GetAstraDatabaseResultOutput) DataEndpointUrl() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.DataEndpointUrl }).(pulumi.StringOutput)
}

// Astra Database ID (system generated)
func (o GetAstraDatabaseResultOutput) DatabaseId() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.DatabaseId }).(pulumi.StringOutput)
}

// Map of Datacenter IDs. The map key is "cloud_provider.region". Example: "GCP.us-east4".
func (o GetAstraDatabaseResultOutput) Datacenters() pulumi.StringMapOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) map[string]string { return v.Datacenters }).(pulumi.StringMapOutput)
}

// URL for the grafana dashboard for this database
func (o GetAstraDatabaseResultOutput) GrafanaUrl() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.GrafanaUrl }).(pulumi.StringOutput)
}

// Graphql URL
func (o GetAstraDatabaseResultOutput) GraphqlUrl() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.GraphqlUrl }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetAstraDatabaseResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.Id }).(pulumi.StringOutput)
}

// Initial keyspace
func (o GetAstraDatabaseResultOutput) Keyspace() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.Keyspace }).(pulumi.StringOutput)
}

// Database name (user provided)
func (o GetAstraDatabaseResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.Name }).(pulumi.StringOutput)
}

// Node count (not relevant for serverless databases)
func (o GetAstraDatabaseResultOutput) NodeCount() pulumi.IntOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) int { return v.NodeCount }).(pulumi.IntOutput)
}

// Ordg id (system generated)
func (o GetAstraDatabaseResultOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.OrganizationId }).(pulumi.StringOutput)
}

// Owner id (system generated)
func (o GetAstraDatabaseResultOutput) OwnerId() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.OwnerId }).(pulumi.StringOutput)
}

// Cloud provider region. Get list of supported regions from regions data-source
func (o GetAstraDatabaseResultOutput) Regions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) []string { return v.Regions }).(pulumi.StringArrayOutput)
}

// Replication Factor (not relevant for serverless databases)
func (o GetAstraDatabaseResultOutput) ReplicationFactor() pulumi.IntOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) int { return v.ReplicationFactor }).(pulumi.IntOutput)
}

// Database status
func (o GetAstraDatabaseResultOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.Status }).(pulumi.StringOutput)
}

// Storage Capacity (not relevant for serverelss databases)
func (o GetAstraDatabaseResultOutput) TotalStorage() pulumi.IntOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) int { return v.TotalStorage }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(GetAstraDatabaseResultOutput{})
}
