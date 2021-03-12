# Overview

ARO demo using ODH and Azure data services

## Instructions

Create service principal and grant access to data
# https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-directory-file-acl-python

Copy data to storage account

```bash
azcopy login --tenant-id=
azcopy make 'https://datalake555.dfs.core.windows.net/mycontainer'
azcopy copy iris.data 'https://datalake555.dfs.core.windows.net/mycontainer/sample/iris.data'
```

Configure anonymous access to storage container
# https://docs.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure?tabs=portal

## TODO 

* Add Kubeflow on Tekton pipeline
* Add model validation and model update to the pipeline
* Add Spark connection to Azure Data Lake
