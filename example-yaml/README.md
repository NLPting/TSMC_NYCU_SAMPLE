# Example of CronJob With Persistent Volume

```
# Apply example PVC to cluster (如果你的GCP Kluste已經掛好PVC,這一步不需做)
kubectl apply -f pvc-demo.yaml

# Apply example Cronjob to cluster (目前yml cronjob，每一分鐘跑一次, 如果要改,直接去yml設定修正)
kubectl apply -f cronjob-pvc.yaml 
kubectl get pod

# 假設不跑了，or 重新部屬Cronjob Pod，需要刪除，可參考此指令
kubectl delete -f cronjob-pvc.yaml 

# 


# To copy things from GKE POD to local
# kubectl cp [POD_NAME]:[FILE_PATH] [LOCAL_PATH]
# One option is to host a dummy POD and copy from it
# kubectl apply -f pod.yaml
kubectl cp ubuntu:/var/log/history/04\:16\:37.xlsx /Users/me/tsmc/TSMC_NYCU_SAMPLE/out.xlsx
```
