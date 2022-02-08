### chlalice + EC2 api wrapper

#### 아키텍쳐

```
HTTP 요청 -> serverless(api gateway + lambda) -> EC2 api 서버 -> 결과 수신
```

#### EC2
- FastAPI > server 폴더
- nginx > Nginx 폴더
- gunicorn > 멀티 프로세스 용
- uvicorn > 단일 프로세스 > 이번 프로젝트에서는 하지 않음
    - gunicorn 사용을 위해 docker-compose 에 ```command: gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000``` 로 RUN

#### serverless
- API Gateway
- lambda

#### 실행 serverless 배포
```
chalice deploy
```

#### EC2 컨테이너 빌드 및 배포
```
docker-compose up -d --build
```
#### Trouble shooting
- cors 설정은 왜인지 몰라도 초반 cors config 설정을 잘 해주고 deploy 를 해야함
- 그렇지 않으면 지우고 새로 만드는 방법으로 해결하는 것이 빠름

#### TODO
- [ ] aws lightsail 적용
- [ ] 기계학습시 sagemaker 적용