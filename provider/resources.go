// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package astra

import (
	"fmt"
	"path/filepath"

	"github.com/mapped/pulumi-astra/provider/pkg/version"
	"github.com/mapped/terraform-provider-astra/v2/provider"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "astra"
	// modules:
	mainMod = "index" // the astra module
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
	return nil
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(provider.New(version.Version)())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:    p,
		Name: "astra",
		// DisplayName is a way to be able to change the casing of the provider
		// name when being displayed on the Pulumi registry
		DisplayName: "",
		// The default publisher for all packages is Pulumi.
		// Change this to your personal name (or a company name) that you
		// would like to be shown in the Pulumi Registry if this package is published
		// there.
		Publisher: "Mapped",
		// LogoURL is optional but useful to help identify your package in the Pulumi Registry
		// if this package is published there.
		//
		// You may host a logo on a domain you control or add an SVG logo for your package
		// in your repository and use the raw content URL for that file as your logo URL.
		LogoURL: "",
		// PluginDownloadURL is an optional URL used to download the Provider
		// for use in Pulumi programs
		// e.g https://github.com/org/pulumi-provider-name/releases/
		PluginDownloadURL: "https://github.com/mapped/pulumi-astra/releases/",
		Description:       "A Pulumi package for creating and managing astra cloud resources.",
		// category/cloud tag helps with categorizing the package in the Pulumi Registry.
		// For all available categories, see `Keywords` in
		// https://www.pulumi.com/docs/guides/pulumi-packages/schema/#package.
		Keywords:   []string{"pulumi", "astra", "category/cloud"},
		License:    "Apache-2.0",
		Homepage:   "https://www.pulumi.com",
		Repository: "https://github.com/mapped/pulumi-astra",
		// The GitHub Org for the provider - defaults to `terraform-providers`
		GitHubOrg:               "mapped",
		TFProviderModuleVersion: "v2",
		Config:                  map[string]*tfbridge.SchemaInfo{
			// Add any required configuration here, or remove the example below if
			// no additional points are required.
			// "region": {
			// 	Type: tfbridge.MakeType("region", "Region"),
			// 	Default: &tfbridge.DefaultInfo{
			// 		EnvVars: []string{"AWS_REGION", "AWS_DEFAULT_REGION"},
			// 	},
			// },
		},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			"astra_access_list":           {Tok: tfbridge.MakeResource(mainMod, mainPkg, "AccessList")},
			"astra_database":              {Tok: tfbridge.MakeResource(mainMod, mainPkg, "Database")},
			"astra_keyspace":              {Tok: tfbridge.MakeResource(mainMod, mainPkg, "Keyspace")},
			"astra_private_link":          {Tok: tfbridge.MakeResource(mainMod, mainPkg, "PrivateLink")},
			"astra_private_link_endpoint": {Tok: tfbridge.MakeResource(mainMod, mainPkg, "PrivateLinkEndpoint")},
			"astra_role":                  {Tok: tfbridge.MakeResource(mainMod, mainPkg, "Role")},
			"astra_token":                 {Tok: tfbridge.MakeResource(mainMod, mainPkg, "Token")},
			"astra_cdc":                   {Tok: tfbridge.MakeResource(mainMod, mainPkg, "Cdc")},
			"astra_streaming_tenant":      {Tok: tfbridge.MakeResource(mainMod, mainPkg, "StreamingTenant")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"astra_access_list":               {Tok: tfbridge.MakeDataSource(mainMod, mainPkg, "getAccessList")},
			"astra_available_regions":         {Tok: tfbridge.MakeDataSource(mainMod, mainPkg, "getAvailableRegions")},
			"astra_database":                  {Tok: tfbridge.MakeDataSource(mainMod, mainPkg, "getAstraDatabase")},
			"astra_databases":                 {Tok: tfbridge.MakeDataSource(mainMod, mainPkg, "getAstraDatabases")},
			"astra_keyspace":                  {Tok: tfbridge.MakeDataSource(mainMod, mainPkg, "getKeyspace")},
			"astra_keyspaces":                 {Tok: tfbridge.MakeDataSource(mainMod, mainPkg, "getKeyspaces")},
			"astra_private_link_endpoints":    {Tok: tfbridge.MakeDataSource(mainMod, mainPkg, "getPrivateLinkEndpoints")},
			"astra_private_links":             {Tok: tfbridge.MakeDataSource(mainMod, mainPkg, "getPrivateLinks")},
			"astra_role":                      {Tok: tfbridge.MakeDataSource(mainMod, mainPkg, "getRoles")},
			"astra_secure_connect_bundle_url": {Tok: tfbridge.MakeDataSource(mainMod, mainPkg, "getSecureConnectBundleUrl")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/mapped/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
