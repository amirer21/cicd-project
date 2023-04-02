# cicd-project

Docker Jenkins CI/CD

#도커 명령어
docker ps
docker container exec -it 'docker container id를 입력' bash

![image](https://user-images.githubusercontent.com/47144594/229289296-2bc907ee-9594-4e01-9e98-9f47278e5296.png)


#git 설정
![image](https://user-images.githubusercontent.com/47144594/229289097-fadb54a3-eb6c-4dfa-9f4d-f8e090f34949.png)


#배포 설정
- ip 주소는 변경될 수 있으므로 확인할 것.
- 127.0.0.1 이 아닌 WAS(tomcat)이 있는 서버의 아이피
![image](https://user-images.githubusercontent.com/47144594/229289048-8c0fcad4-f3a3-43d1-be9e-8d159ae006d4.png)


#자동 빌드
- 스케줄러에 따라 git에서 변경사항이 있는 경우 빌드 및 배포
![image](https://user-images.githubusercontent.com/47144594/229289142-2d518bc3-0e73-4526-b6a6-f9dd4a8a8ae4.png)

#빌드 방식
- clean, complile, package
![image](https://user-images.githubusercontent.com/47144594/229289177-ac911690-960b-4c79-9b20-2a1b9d765419.png)

#pipeline
- plugin : delivery pipeline
- 각각의 job에서 빌드 후 조치 : Build other projects > Trigger only if build is stable

#pipe-line script
pipeline {
    agent any //실행가능한 어느 서버에서든 pipeline 실행
    stages {
        stage('build') {
           //build stage 선언
        }
        stage('test') {
          //test stage 선언
        }
        stage('deploy') {
           //deploy stage 선언
        }
    }
}
