kubectl delete deployment,pods,services -l app=rps
echo sleep 5 secs
sleep 5

kubectl apply -f front-service.yaml
kubectl apply -f user-service.yaml
kubectl apply -f back-service.yaml
kubectl apply -f bot-service.yaml
