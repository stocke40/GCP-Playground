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
stocke@MSI MINGW64 ~/gitrepos/GCP-Playground (InitialCommit)
$ curl -X POST https://us-central1-greg-play-gcp-project.cloudfunctions.net/CME_quote_ES -H "Content-Type:application/json" -d '{"name":"PLTR"}'
Hello PLTR!
grego@MSI MINGW64 ~/gitrepos/GCP-Playground (InitialCommit)
$
```

My notes going through this process are in [this Google Doc](https://docs.google.com/document/d/1Dhes1b-NZqqArBgByggriFyyUjTLHyeNwu2VEglYkFc/edit#heading=h.fb1psvpelt68).

## Deploying from (Mirrored) Google Cloud Source Repository

Once changes are committed to the local repository, pushed to the remote repositiory on github, then mirrored to the connected Google Cloud Source Repository, they must be deployed before they can actually run as a google cloud function.

The below command deploys changes committed and pushed to the InitialCommit branch of the github_stocke40_gcp-playground google cloud source repository to the CME_quote_ES google cloud function:  

```Shell
stocke@MSI MINGW64 ~/gitrepos/GCP-Playground (InitialCommit)
$ gcloud functions deploy CME_quote_ES \
  --source https://source.developers.google.com/projects/greg-play-gcp-project/repos/github_stocke40_gcp-playground/moveable-aliases/InitialCommit/paths/functions/CME_quote_ES \
  --region=us-central1 \
  --trigger-http \
  --runtime python37 \
  --entry-point CME_quote_ES \
  --allow-unauthenticated
```

After successful deploy, the changed google cloud function can be accessed at

https://us-central1-greg-play-gcp-project.cloudfunctions.net/CME_quote_ES