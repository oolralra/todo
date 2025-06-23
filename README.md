# 🛠️ Svelte + FastAPI + MariaDB Todo App

간단한 **Svelte + FastAPI + MariaDB** 구조의 모놀리식 웹 애플리케이션입니다.  
각 컴포넌트는 Docker 컨테이너로 구성되어 있으며, `docker-compose`를 통해 실행됩니다.

## 🚀 실행 방법

```bash
docker compose up -d --build

DB컨테이너 준비에 시간이 걸려 백엔드 컨테이너가 안뜨는 경우도 있으니 그런 경우엔 up을 한번 더 하면 된다
