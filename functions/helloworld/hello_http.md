# hello_http

An initial "Hello World" google cloud function.

hello_http deployed to:
<https://us-central1-greg-play-gcp-project.cloudfunctions.net/hello_http>
on 31-Jan 2021.

sample execution:

```Shell
curl -X POST https://us-central1-greg-play-gcp-project.cloudfunctions.net/hello_http -H "Content-Type:application/json" -d '{"name":"PLTR"}'
```

```Shell
grego@MSI MINGW64 ~/gitrepos/GCP-Playground (InitialCommit)
$ curl -X POST https://us-central1-greg-play-gcp-project.cloudfunctions.net/hello_http -H "Content-Type:application/json" -d '{"name":"PLTR"}'
Hello PLTR!
grego@MSI MINGW64 ~/gitrepos/GCP-Playground (InitialCommit)
$
```

My notes going through this process are in [this Google Doc](https://docs.google.com/document/d/1Dhes1b-NZqqArBgByggriFyyUjTLHyeNwu2VEglYkFc/edit#heading=h.fb1psvpelt68).

## Deploying from (Mirrored) Google Cloud Source Repository
