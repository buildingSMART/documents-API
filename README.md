[![Official repository by buildingSMART International](https://img.shields.io/badge/buildingSMART-Official%20Repository-orange.svg)](https://www.buildingsmart.org/)
[![This repo is managed by the BCF Implementers Group](https://img.shields.io/badge/-BCF%20Implementers%20Group-blue.svg)](https://img.shields.io/badge/-BCF%20Implementers%20Group-blue.svg)

[Swagger / OpenAPI Specification](./swagger.yaml). To view an interactive version of the Swagger specification, you can go to <https://editor.swagger.io/> and pase the content from the YAML file.

> **TODO** Host the Swagger Spec directly, would improve the UX here. Maybe via GitHub pages? Or we could provide a static site.

> **TODO** Decide on whether to call it _Documents API_ or _DocumentsAPI_

# Documents API

<img src="./Images/CDE_Logo.png" width="200" height="200">

> **TODO** Logo😀 Need to wait for bSI to either provide one or approve the proposed logo.

The Documents API is designed to streamline the process of downloading and uploading files to a common data environment (CDE). This specification details the _selection_ or _discovery_, _download_ and _upload_ of files. When supported by both client and server, it provides an easy to use and integrated way of syncing cloud stored documents from within local applications. For the purpose of this specification a Documents consists of a file and its metadata.The scope of the Documents API includes all file types; The scope is not limited to building information models.

## Contributing

The Open CDE workgroup develops the BCF standard. The group meets every second Monday at 11am CET. To join the fortnightly meeting please email [opencde@buildingsmart.org](mailto:opencde@buildingsmart.org).

<!-- toc  https://ecotrust-canada.github.io/markdown-toc/ -->

- [Documents API](#documents-api)
  - [Contributing](#contributing)
- [1. Introduction](#1-introduction)
  - [1.1. OpenCDE Foundation API](#11-opencde-foundation-api)
  - [1.2 Using Documents API and BCF API Together](#12-using-documents-api-and-bcf-api-together)
- [2. Overview](#2-overview)
  - [Use Cases](#use-cases)
  - [How does the Document API work?](#how-does-the-document-api-work)
- [3. Services](#3-services)
  - [3.1 Open API Specification - The Single Source of Truth](#31-open-api-specification---the-single-source-of-truth)
  - [3.2. Document Download](#32-document-download)
    - [3.2.1. Document Download Example](#321-document-download-example)
  - [3.3. Document Upload](#33-document-upload)
    - [3.3.1. Document Upload Example](#331-document-upload-example)
    - [Multipart Upload Considerations & Implementation Notes](#multipart-upload-considerations--implementation-notes)
- [4. Acknowledgements / History](#4-acknowledgements--history)
<!-- tocstop -->

# 1. Introduction

## 1.1. OpenCDE Foundation API

Documents API is a member of the OpenCDE API family. All OpenCDE APIs are united by a shared common API called [OpenCDE Foundation API](https://github.com/buildingSMART/foundation-API).  
The foundation API specifies a small number of services and a few conventions that are common to all OpenCDE APIs. All Documents API implementations must implement the Foundation API and follow its conventions and guidelines. Implementers should start by implementing the Foundation API and only then continue to implement the Documents API.

> Note: Other APIs built on top of the OpenCDE Foundation API include the [BCF API for the BIM Collaboration Format](https://github.com/buildingSMART/BCF-API).

## 1.2 Using Documents API and BCF API Together

Documents API and BCF API can be used at the same time in a client software that has implemented both APIs. If you are working in a project that uses a service that implements both, you can get the BIM files (e.g., IFCs) directly from the service with the Documents API and create issues about them using the BCF API. You can also have a configuration, where your documents reside in a service that only supports the Documents API and your communicate about the issues with another service that supports BCF API.

# 2. Overview

The Documents API identifies the following actors:

- User - A human, performing a task requiring the download or the upload of files
- Client Application - A desktop Application or a Web Application used by the User to perform her task
- Common Data Environment (CDE or Server) - A cloud application hosting files for a construction project

![Documents API Topology](./Images/CDE_Overview_Diagram.png)

> **TODO** Replace the diagram above with an image that correctly shows the three actors described above

## Use Cases

The Documents API is designed to support the following use cases:

- File Download - The User, using the Application searches files on the CDE and selects files to download. The Application then downlods the files and makes them available to the User in the Application.
- File Upload - The User, using the Application, selects local files to upload to the CDE. The Application directs to user to the CDE Web UI. The user enters the document metadata on the CDE. The Application then uploads the file to the CDE. The CDE combines the file with the user-entered metadata and registers a new document.
- Automatic download of a file previously uploaded or downloaded - The Application detects, using previously stored information, that a new version exists. The Application (with the User's approval) downloads the new version and makes the files available to the User.

Not yet supported: Automatic syncing of documents between two or more CDEs will be added in the future.

## How does the Document API work?

The Documents API is designed to allow the User working with any Client Applications to upload and download files on any CDE. This is accomplished by a file-based API between the Application and CDE. The Documents API also includes a hand-shake that would allow the Application to direct the User to the CDE's web interface when needed. For example: when commencing a document download the user would search and select Documents on the CDE's web interface. The actual file download is then performed in a direct API call by the Application

> **TODO** Add a short diagram, showing maybe files flowing (with arrows?) between these two.

# 3. Services

> **TODO** Mention that the spec doesn't make any assumptions about concurrency is handled, e.g. two users trying to upload a document version at the same time. Also think where to put this paragraph😀

## 3.1 Open API Specification - The Single Source of Truth

Documents API is specified using [Open API](https://www.openapis.org/). You can find the Open API specification [here](swagger.yaml). The specification can be used to automatically generate client and server code, although most of the endpoints will not work directly, since the API is built with few fixed endpoints. Most of the endpoints are discovered and received in the returned payloads of the calls. The dynamic endpoints start with `server-provided-path-`.
The motivation for using dynamic endpoints is to make the implementation of the API on the server easy and efficient. For example, when a link to download a document is retrieved from the service, that link can point to an already existing API end point, or event to a third parth file hosting service.

The Open API specification is the single source of truth for implementing the Documents API. This documentation is supporting material that clarifies different workflows. If there are any contradictions between this document and the swagger specification, the latter prevails.

> **TODO** Explain how to use the Swagger spec, especially with regard to the dynamic urls.

> **TODO** Link the open source implementation, mention how it's supported (expect bugs, but those will be addressed)

## 3.2. Document Download

> **TODO** Text description, and flow sequence diagram.

### 3.2.1. Document Download Example

![Document Download Sequence Diagram](./Diagrams/Document_Download.png)

> **TODO** Add examples, with requests and maybe mock up "screenshots". Maybe move examples to a different file and just link it here, to avoid cluttering.

> **TODO** See <https://github.com/buildingSMART/BCF-API#331-get-project-files-information-service>, we should make the _reference_ from the BCF-API be the url that is returned here for the download as to better integrate the two APIs,

## 3.3. Document Upload

> **TODO** Text description, and flow sequence diagram.

### 3.3.1. Document Upload Example

> **TODO** Add examples, with requests and maybe mock up "screenshots". Maybe move examples to a different file and just link it here, to avoid cluttering.

### Multipart Upload Considerations & Implementation Notes

> **TODO** Explain why we did it the way we did it😀 Should cover: Multiple storage providers, direct upload without going through compute, upload in multiple parts due to size restrictions

# 4. Acknowledgements / History

> **TODO** Maybe list companies that contributed in the original DocumentsAPI Project in 2021/2022?
