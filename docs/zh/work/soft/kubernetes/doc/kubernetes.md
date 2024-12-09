# minikube

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-latest.x86_64.rpm
sudo rpm -Uvh minikube-latest.x86_64.rpm


minikube start

minikube kubectl -- get po -A

minikube dashboard

minikube kubectl -- proxy --port=8001 --address='192.168.3.204' --accept-hosts='^.*' 

http://192.168.3.204:8001//api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/