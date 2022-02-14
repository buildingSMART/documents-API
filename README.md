[![Official repository by buildingSMART International](https://img.shields.io/badge/buildingSMART-Official%20Repository-orange.svg)](https://www.buildingsmart.org/)
[![This repo is managed by the BCF Implementers Group](https://img.shields.io/badge/-BCF%20Implementers%20Group-blue.svg)](https://img.shields.io/badge/-BCF%20Implementers%20Group-blue.svg)

[Swagger / OpenAPI Specification](./swagger.yaml). To view an interactive version of the Swagger specification, you can go to <https://editor.swagger.io/> and pase the content from the YAML file.

> **TODO** Host the Swagger Spec directly, would improve the UX here. Maybe via GitHub pages? Or we could provide a static site.

> **TODO** Decide on whether to call it _Documents API_ or _DocumentsAPI_

# Documents API

![Documents API Logo](./Images/CDE_Logo.png)

> **TODO** Logo😀 Need to wait for bSI to either provide one or approve the proposed logo.

The Documents API is an interactive way of syncing documents between client applications and CDEs. It's specification details the _selection_ or _discovery_, _download_ and _upload_ of documents and files. When supported by both client and server, it provides an easy to use and integrated way of working on cloud stored documents from within local applications. Documents here refers to files, meaning the scope is not only limited to building models but any files.

## Contributing

The Open CDE workgroup develops the BCF standard. The group meets every second Monday at 11am CET. To join the fortnightly meeting please email [opencde@buildingsmart.org](mailto:opencde@buildingsmart.org).

<!-- toc  https://ecotrust-canada.github.io/markdown-toc/ -->
- [Documents API](#documents-api)
  * [Contributing](#contributing)
- [1. Introduction](#1-introduction)
  * [1.1. OpenCDE Foundation API](#11-opencde-foundation-api)
- [2. Topology](#2-topology)
- [3. Services](#3-services)
  * [3.1 Swagger Specification - How To](#31-swagger-specification---how-to)
  * [3.2. Document Selection](#32-document-selection)
    + [3.2.1. Document Selection Example](#321-document-selection-example)
  * [3.3. Document Download](#33-document-download)
    + [3.3.1. Document Download Example](#331-document-download-example)
  * [3.4. Document Upload](#34-document-upload)
    + [3.4.1. Document Upload Example](#341-document-upload-example)
    + [Multipart Upload Considerations & Implementation Notes](#multipart-upload-considerations---implementation-notes)
- [4. Acknowledgements / History](#4-acknowledgements---history)
<!-- tocstop -->

# 1. Introduction

## 1.1. OpenCDE Foundation API

Documents API is a member of the OpenCDE API family. All OpenCDE APIs are united by a shared common API called [OpenCDE Foundation API](https://github.com/buildingSMART/foundation-API).  
The foundation API specifies a small number of services and a few conventions that are common to all OpenCDE APIs. All Documents API implementations must implement the Foundation API and follow its conventions and guidelines. Implementers should start by implementing the Foundation API and only then continue to implement the Documents API.

> Note: Other APIs built on top of the OpenCDE Foundation API include the [BCF API for the BIM Collaboration Format](https://github.com/buildingSMART/BCF-API).

## 1.2 Using Documents API and BCF API Together** 

Documents API and BCF API can be used at the same time in a client software that has implemented both APIs. If you are working in a project that uses a service that implements both, you can get the BIM files (e.g., IFCs) directly from the service with the Documents API and create issues about them using the BCF API. You can also have a configuration, where your documents reside in a service that only supports the Documents API and your communicate about the issues with another service that supports BCF API.


# 2. Topology

![Documents API Topology](./Images/CDE_Overview_Diagram.png)

> **TODO** Have a short paragraph describing the client-server setup / relationship and maybe also a short diagram, showing maybe files flowing (with arrows?) between these two.

> **TODO** List use cases, also explicitly list that automatic server-to-server syncing is not part of this API. Mention also that future versions (or other APIs?) will add this feature.

# 3. Services

> **TODO** Mention that the spec doesn't make any assumptions about concurrency is handled, e.g. two users trying to upload a document version at the same time. Also think where to put this paragraph😀

## 3.1 Swagger Specification - How To

> **TODO** Explain how to use the Swagger spec, especially with regard to the dynamic urls.

> **TODO** Link the open source implementation, mention how it's supported (expect bugs, but those will be addressed)

## 3.2. Document Selection

> **TODO** Text description, and flow sequence diagram.

### 3.2.1. Document Selection Example

> **TODO** Add examples, with requests and maybe mock up "screenshots". Maybe move examples to a different file and just link it here, to avoid cluttering.

## 3.3. Document Download

> **TODO** Text description, and flow sequence diagram.

> **TODO** See <https://github.com/buildingSMART/BCF-API#331-get-project-files-information-service>, we should make the _reference_ from the BCF-API be the url that is returned here for the download as to better integrate the two APIs,

### 3.3.1. Document Download Example

> **TODO** Add examples, with requests and maybe mock up "screenshots". Maybe move examples to a different file and just link it here, to avoid cluttering.

## 3.4. Document Upload

> **TODO** Text description, and flow sequence diagram.

### 3.4.1. Document Upload Example

> **TODO** Add examples, with requests and maybe mock up "screenshots". Maybe move examples to a different file and just link it here, to avoid cluttering.

### Multipart Upload Considerations & Implementation Notes

> **TODO** Explain why we did it the way we did it😀 Should cover: Multiple storage providers, direct upload without going through compute, upload in multiple parts due to size restrictions

# 4. Acknowledgements / History

> **TODO** Maybe list companies that contributed in the original DocumentsAPI Project in 2021/2022?
