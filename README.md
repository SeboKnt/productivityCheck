# productivityCheck

## reproduce:

helm repo add cnpg https://cloudnative-pg.github.io/charts
helm upgrade --install cnpg \
  --namespace cnpg-system \
  --create-namespace \
  cnpg/cloudnative-pg


https://cloudnative-pg.io/documentation/1.20/quickstart/

helm repo add prometheus-community \
  https://prometheus-community.github.io/helm-charts

helm upgrade --install \
  -f https://raw.githubusercontent.com/cloudnative-pg/cloudnative-pg/main/docs/src/samples/monitoring/kube-stack-config.yaml \
  prometheus-community \
  prometheus-community/kube-prometheus-stack


kubectl get secret sql-superuser -o jsonpath="{.data.username}" | base64 -d
kubectl get secret sql-superuser -o jsonpath="{.data.password}" | base64 -d
kubectl get secret sql-app -o jsonpath="{.data.username}" | base64 -d
kubectl get secret sql-app -o jsonpath="{.data.password}" | base64 -d

$ kubectl get all
NAME                           READY   STATUS    RESTARTS   AGE
[...]
service/sql-rw       ClusterIP   10.43.90.174    <none>        5432/TCP   8h

psql -h 10.43.90.174 -p 5432 -U postgres -W postgres


### wir müssen ein secret erstellen damit wir von privaten ziehen können
kubectl create secret docker-registry github-pull-secret \
  --docker-server=ghcr.io \
  --docker-username=YOUR_GITHUB_USERNAME \
  --docker-password=YOUR_GITHUB_ACCESS_TOKEN

### wenn wir ein neues deployment haben:
kubectl rollout restart deployment mqtt2db

