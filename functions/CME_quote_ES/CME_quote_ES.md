# CME_Quote_ES

Google cloud function to get the prior setlement of the /ES contract.

CME_quote_ES deployed to:
<https://us-central1-greg-play-gcp-project.cloudfunctions.net/CME_quote_ES>
on 31-Jan 2021.

sample execution:

```Shell
curl -X POST https://us-central1-greg-play-gcp-project.cloudfunctions.net/CME_quote_ES -H "Content-Type:application/json" -d '{"name":"PLTR"}'
```

```Shell
grego@MSI MINGW64 ~/gitrepos/GCP-Playground (InitialCommit)
$ curl -X POST https://us-central1-greg-play-gcp-project.cloudfunctions.net/CME_quote_ES -H "Content-Type:application/json" -d '{"name":"PLTR"}'
Hello PLTR!
grego@MSI MINGW64 ~/gitrepos/GCP-Playground (InitialCommit)
$
```

My notes going through this process are in [this Google Doc](https://docs.google.com/document/d/1Dhes1b-NZqqArBgByggriFyyUjTLHyeNwu2VEglYkFc/edit#heading=h.fb1psvpelt68).

## Deploying from (Mirrored) Google Cloud Source Repository

https://us-central1-greg-play-gcp-project.cloudfunctions.net/CME_quote_ES

Still working on the below gcloud CLI deploy

'''Shell
grego@MSI MINGW64 ~/gitrepos/GCP-Playground (InitialCommit)
$ gcloud functions deploy CME_quote_ES \
  --source https://source.developers.google.com/projects/greg-play-gcp-project/repos/github_stocke40_gcp-playground/moveable-aliases/InitialCommit/paths/functions/CME_quote_ES \
  --region=us-central1 \
  --trigger-http \
  --runtime python37 \
  --entry-point CME_quote_ES \
  --allow-unauthenticated
'''
