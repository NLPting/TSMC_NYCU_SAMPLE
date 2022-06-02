# Example of CronJob With Persistent Volume

```
# Apply example PVC to cluster
kubectl apply -f pvc-demo.yaml

# Apply example Cronjob to cluster
kubectl apply -f cronjob-pvc.yaml

# To copy things from GKE POD to local
# kubectl cp [POD_NAME]:[FILE_PATH] [LOCAL_PATH]
# One option is to host a dummy POD and copy from it
# kubectl apply -f pod.yaml
kubectl cp ubuntu:/var/log/history/04\:16\:37.xlsx /Users/me/tsmc/TSMC_NYCU_SAMPLE/out.xlsx
```