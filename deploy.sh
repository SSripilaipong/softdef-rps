kubectl delete deployment,pods,services -l app=rps
echo sleep 20 secs
sleep 20

kubectl apply -f user-service.yaml
kubectl apply -f back-service.yaml
kubectl apply -f bot-service.yaml
kubectl apply -f front-service.yaml
