# GCP-Playground

Playground to experiment with Google Cloud Functions.

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
