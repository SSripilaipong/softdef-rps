docker build -t shsnail/softdef-rps-front front
docker build -t shsnail/softdef-rps-user user
docker build -t shsnail/softdef-rps-back back
docker build -t shsnail/softdef-rps-bot bot

docker push shsnail/softdef-rps-front
docker push shsnail/softdef-rps-user
docker push shsnail/softdef-rps-back
docker push shsnail/softdef-rps-bot
