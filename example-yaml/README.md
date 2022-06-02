# Example of CronJob With Persistent Volume

```
# Apply example PVC to cluster (如果你的GCP Kluste已經掛好PVC,這一步不需做)
kubectl apply -f pvc-demo.yaml

# Apply example Cronjob to cluster (目前yml cronjob，每一分鐘跑一次, 如果要改,直接去yml設定修正)
kubectl apply -f cronjob-pvc.yaml 

# 監控POD運行狀況，以及確定自己的cronJob Pod是否執行完成
kubectl get pod

# 假設不跑了，or 重新部屬Cronjob Pod，需要刪除，可參考此指令
kubectl delete -f cronjob-pvc.yaml 

# 假設跑完了，需要把檔案，下載到Local去做分析:
(一)先去確認，CronJob執行完後，有成功下載到Base Container上
1. kubectl exec -it ubuntu bash (進到Container環境)
2. cd /var/log/history  (切入到PVC掛載位置)
3. 找到檔案 04:16:37.xlsx (程式是用時間命名檔案，這邊by你需求改成crawler程式)
4. exit (離開Container環境)

(二) Local下載:
To copy things from GKE POD to local
kubectl cp [POD_NAME]:[FILE_PATH] [LOCAL_PATH]
1. kubectl cp ubuntu:/var/log/history/04\:16\:37.xlsx /Users/me/tsmc/TSMC_NYCU_SAMPLE/out.xlsx


```
