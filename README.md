[![Official repository by buildingSMART International](https://img.shields.io/badge/buildingSMART-Official%20Repository-orange.svg)](https://www.buildingsmart.org/)
[![This repo is managed by the BCF Implementers Group](https://img.shields.io/badge/-BCF%20Implementers%20Group-blue.svg)](https://img.shields.io/badge/-BCF%20Implementers%20Group-blue.svg)

[Swagger / OpenAPI Specification](./swagger.yaml). To view an interactive version of the Swagger specification, you can go to <https://editor.swagger.io/> and pase the content from the YAML file.

> **TODO** Host the Swagger Spec directly, would improve the UX here. Maybe via GitHub pages? Or we could provide a static site.

# Documents API

<img src="./Images/CDE_Logo.png" width="200" height="200">

> **TODO** Logo😀 Need to wait for bSI to either provide one or approve the proposed logo.

The Documents API is designed to streamline the process of downloading and uploading files to a common data environment (CDE). This specification details the _selection_ or _discovery_, _download_ and _upload_ of files. When supported by both client and server, it provides an easy to use and integrated way of syncing cloud stored documents from within local applications. For the purpose of this specification a Documents consists of a file and its metadata.The scope of the Documents API includes all file types; The scope is not limited to building information models.

## Contributing

The Open CDE workgroup develops the BCF standard. The group meets every second Monday at 11am CET. To join the fortnightly meeting please email [opencde@buildingsmart.org](mailto:opencde@buildingsmart.org).

<!-- toc  https://ecotrust-canada.github.io/markdown-toc/ -->

- [Documents API](#documents-api)
  * [Contributing](#contributing)
- [1. Introduction](#1-introduction)
  * [1.1. OpenCDE Foundation API](#11-opencde-foundation-api)
- [2. Overview](#2-overview)
  * [2.1 How does the Document API work?](#21-how-does-the-document-api-work)
  * [2.2 Use Cases](#22-use-cases)
    + [2.2.1 Download Files](#221-download-files)
      - [2.2.1.1 Automatic download of a file previously uploaded or downloaded](#2211-automatic-download-of-a-file-previously-uploaded-or-downloaded)
    + [2.2.2 Upload Files](#222-upload-files)
    + [2.2.3 Using Documents API and BCF API Together](#223-using-documents-api-and-bcf-api-together)
      - [2.2.3.1 BCF File References](#2231-bcf-file-references)
    + [2.2.4 Automatic syncing of documents between two or more CDEs](#224-automatic-syncing-of-documents-between-two-or-more-cdes)
- [3. Services](#3-services)
  * [3.1 Open API Specification - The Single Source of Truth](#31-open-api-specification---the-single-source-of-truth)
  * [3.2. Document Download](#32-document-download)
    + [3.2.1. Document Download Example](#321-document-download-example)
  * [3.3. Document Upload](#33-document-upload)
    + [3.3.1. Document Upload Example](#331-document-upload-example)
    + [Multipart Upload Considerations & Implementation Notes](#multipart-upload-considerations---implementation-notes)
- [4. Acknowledgements / History](#4-acknowledgements---history)

markdown-toc</a></i></small>
<!-- tocstop -->

# 1. Introduction

## 1.1. OpenCDE Foundation API

Documents API is a member of the OpenCDE API family. All OpenCDE APIs are united by a shared common API called [OpenCDE Foundation API](https://github.com/buildingSMART/foundation-API).  
The foundation API specifies a small number of services and a few conventions that are common to all OpenCDE APIs. All Documents API implementations must implement the Foundation API and follow its conventions and guidelines. Implementers should start by implementing the Foundation API and only then continue to implement the Documents API.

> Note: Other APIs built on top of the OpenCDE Foundation API include the [BCF API for the BIM Collaboration Format](https://github.com/buildingSMART/BCF-API).

# 2. Overview

The Documents API identifies the following actors:

- User - A human, performing a task requiring the download or the upload of files
- Client Application - A desktop Application or a Web Application used by the User to perform her task
- Common Data Environment (CDE or Server) - A cloud application hosting files for a construction project

![Documents API Topology](./Images/CDE_Overview_Diagram.png)

> **TODO** Replace the diagram above with an image that correctly shows the three actors described above

## 2.1. How does the Document API work?

The Documents API is designed to allow a User working with any Client Applications to upload and download files on any CDE. This is accomplished by a file-based API between the Application and the CDE. The Documents API also includes a hand-shake that would allow the Application to direct the User to the CDE's web interface when needed. For example: when commencing a document download the user would search and select Documents on the CDE's web interface. The actual file download is then performed in a direct API made by the Application to the CDE. 

## 2.2. Use Cases

The Documents API is designed to support the following use cases:

### 2.2.1. Download Files

The User, using the Application searches files on the CDE and selects files to download. The Application then downloads the files and makes them available to the User in the Application.

#### 2.2.1.1. Automatic download of a file previously uploaded or downloaded 

The Application detects, using previously stored information, that new document versions exists. The Application obtains the User's approval and downloads the new version and makes the files available to the User.

### 2.2.2. Upload Files

The User, using the Application, selects local files to upload to the CDE. The Application directs to user to the CDE Web UI. The user enters, for each file, the required document metadata on the CDE. The Application then uploads the files to the CDE. The CDE combines the files with the user-entered metadata and registers a new document.

> **TODO** Add a short diagram, showing maybe files flowing (with arrows?) between these two.

### 2.2.3. Using Documents API and BCF API Together

Documents API and BCF API can be used together in an Application that has implemented both APIs. A user who is working with an Application that implements both APIs can download the Models directly from the CDE using the Documents API and create issues about them using the BCF API. A configuration, where documents are controlled by one CDE and BCF issues are controlled by another CDE is also supported.

#### 2.2.3.1. BCF File References

BCF API compatible servers offer endpoints to list project model files, which are stored on a CDE. To connect the model resolution from BCF API file references with documents stored on a CDE implementing the Documents API, the `reference` part of a `file_GET` is returned by the BCF server with a specific protocol `documents` and a link to the `document_version` url on the CDE server.  
The scheme for the actual request to obtain the document version data is assumed to be `https`.

BCF API `file_GET` example:

```json
{
  "display_information": [
    {
      "field_display_name": "Model Name",
      "field_value": "ARCH-Z100-051"
    }
  ],
  "file": {
    "ifc_project": "0J$yPqHBD12v72y4qF6XcD",
    "file_name": "OfficeBuilding_Architecture_0001.ifc",
    "reference": "documents://<document_version_url>"
  }
}
```

> **TODO** find better protocol name instead of `documents`, since this is likely to clash with something else.

In the example above, the BCF server returns a value of `documents://<document_version_url>` for the file `reference` part, indicating that this is an url that should be accessed with a Documents API capable client to get the document version endpoint. From there on, compatible clients can retrieve metadata and the binary content of the file.

The BCF API section about project file references can be found here: <https://github.com/buildingSMART/BCF-API#331-get-project-files-information-service>

### 2.2.4 Automatic syncing of documents between two or more CDEs 

This use case is not yet supported. It will be added in the future.

# 3. Services

> **TODO** Mention that the spec doesn't make any assumptions about concurrency is handled, e.g. two users trying to upload a document version at the same time. Also think where to put this paragraph😀

## 3.1 Open API Specification - The Single Source of Truth

Documents API is specified using [Open API](https://www.openapis.org/). You can find the Open API specification [here](swagger.yaml). The specification can be used to automatically generate client and server code, although most of the endpoints will not work directly, since the API is built with few fixed endpoints. Most of the endpoints are discovered and received in the returned payloads of the calls. The dynamic endpoints start with `server-provided-path-`.
The motivation for using dynamic endpoints is to make the implementation of the API on the server easy and efficient. For example, when a link to download a document is retrieved from the service, that link can point to an already existing API end point, or event to a third parth file hosting service.

The Open API specification is the single source of truth for implementing the Documents API. This documentation is supporting material that clarifies different workflows. If there are any contradictions between this document and the Open API specification, the latter prevails.

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

![Document Upload Sequence Diagram](./Diagrams/Document_Upload.png)
> **TODO** Add examples, with requests and maybe mock up "screenshots". Maybe move examples to a different file and just link it here, to avoid cluttering.

### Multipart Upload Considerations & Implementation Notes

Uploading documents to CDE is the most complicated workflow in this API. The flow starts with presenting meta data (names and session ids) of the files to be uploaded to the server. After that, the user is presented with browser UI of the CDE, where they can enter any necessary additional meta data that the CDE deems necessary for the documents. When the user is finished entering the meta data a URL is sent to the callback of the client. The client sends a POST to this URL with additional information (size and session id per each file). As return to this call come the upload instructions detailing how each file should be uploaded to the CDE.

#### Identifying Files During the Workflow
The `session_file_id` property used in the components (`FileToUpload`, `UploadFileDetails`, `DocumentToUpload`) related to uploading files is a client-generated identifier that is only used during upload. It doesn't need to be persisted between upload sessions. It is used to relate the information given in different phases of the workflow to the individual files that are being processed.

#### Why This Workflow
The reason why uploading is done in so many steps is to support a use case, where the client software doesn't yet have the local file available, when the upload workflow starts. For example, when a CAD tool would like to export an IFC file to the server. Creating that IFC file can take a long time. With the chosen workflow, the user interaction happens first, and only when the server knows all the necessary meta data, the client software can start creating the file, if it already doesn't exist, and uploading it. Since this process doesn't need interaction, it can happen in the background and doesn't need attention from the user.

# 4. Acknowledgements / History

> **TODO** Maybe list companies that contributed in the original DocumentsAPI Project in 2021/2022?
