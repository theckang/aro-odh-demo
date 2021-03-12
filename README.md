# Overview

ARO demo using [Open Data Hub](https://opendatahub.io/) and Azure data services - Azure Data Lake and Azure Blob Storage.

## Prerequisites

* Azure Red Hat OpenShift 4 Cluster
* Admin access to OpenShift
* [OpenShift CLI](https://docs.openshift.com/container-platform/4.6/cli_reference/openshift_cli/getting-started-cli.html)
* Install [Open Data Hub](https://github.com/theckang/aro-odh-install)

## Setup

Download the [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris).

Create a [storage account with Azure Data Lake](https://docs.microsoft.com/en-us/azure/storage/blobs/create-data-lake-storage-account).

Create a [storage principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#register-an-application-with-azure-ad-and-create-a-service-principal):

* Make sure to assign the `Storage Blob Data Contributor` role to the service principal
* Create a new application secret for authenticating the service principal
* Copy down the `client-id`, `tenant-id`, and `client-secret` values (you will need this later)

View your [account access key](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&tabs=azure-portal#view-account-access-keys) and copy down the storage account's `connection string` (you will need this later)

Download [azcopy](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10?toc=/azure/storage/blobs/toc.json#download-azcopy).

Upload the Iris dataset to Azure Data Lake

> Replace with your tenant-id and storage account name

```bash
azcopy login --tenant-id=<tenant-id> 
azcopy make 'https://<storage-account-name>.dfs.core.windows.net/mycontainer'
azcopy copy iris.data 'https://<storage-account-name>.dfs.core.windows.net/mycontainer/sample/iris.data'
```

Configure [anonymous access](https://docs.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure?tabs=portal#set-the-public-access-level-for-a-container
) to storage container `mycontainer`.

Launch JupyterHub

```bash
echo $(oc get route jupyterhub -n odh --template='http://{{.spec.host}}')
```

Select the s2i-spark-minimal-notebook image and spawn the server. Leave the other settings as they are.

Upload the `model_pipeline.ipynb` notebook.  Set the variables in the second cell where it says `### ENTER YOUR DETAILS ###`.

## TODO 

* Mount a secret with the env variables for the client, tenant, and client secret values
* Add Kubeflow on Tekton pipeline
* Add model validation and model update to the pipeline
* Add Spark connection to Azure Data Lake
