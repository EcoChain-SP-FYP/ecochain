FROM python:3

ENV BLOCKCHAIN_NODE_IP 127.0.0.1
ENV DEPLOYED_CONTRACT_ADDRESS 0

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

COPY . .

CMD "python" "./main.py" ${BLOCKCHAIN_NODE_IP} ${DEPLOYED_CONTRACT_ADDRESS}