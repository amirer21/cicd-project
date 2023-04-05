# Docker Jenkins CI/CD (Java Maven Web Project)

# 순서
## JDK 설치
## Tomcat 설치 및 설정
## Docker 
## Jenkins(Docker) 
## Jenkins 빌드 및 배포
## Jenkins Pipeline (View, Script, Git Script)

# JDK 설치
OpenJDK 설치 - https://jdk.java.net/11/

# Tomcat 설치
https://tomcat.apache.org (9.x 버전 사용)

- Tomcat 설정 변경
- 포트 변경 
경로 : %TOMCAT_HOME%\conf\server.xml
```
    <Connector port="8088" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
```

- 접근 엑세스 변경
- 경로 : %TOMCAT_HOME%\webapps\manager\META-INF\context.xml 
- 경로 : %TOMCAT_HOME%\webapps\host-manager\META-INF\context.xml 

다음 코드를 주석처리 한다.
```
  <!-- <Valve className="org.apache.catalina.valves.RemoteAddrValve"
         allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" /> -->
```

- 유저 추가
%TOMCAT_HOME%\conf\tomcat-users.xml
```
  <role rolename="manager-gui"/>
  <role rolename="manager-script"/>
  <role rolename="manager-jxm"/>
  <role rolename="manager-status"/>
  <user username="admin" password="admin" roles="manager-gui, manager-script, manager-jxm, manager-status"/>
  <user username="deployer" password="deployer" roles="manager-script"/>
  <user username="tomcat" password="tomcat" roles="manager-gui"/>
```

# 도커 설치

- Docker 명령어
* 이미지 목록 확인
```
docker image ls
```

* 컨테이너 목록 확인
```
docker container ls
```

* 네트워크 목록 확인
```
docker network ls 
```

# 도커 Jenkins 설치
1. jenkins 설치
- https://github.com/jenkinsci/docker (github)
- https://www.jenkins.io/download/ 에서 docker 항목으로 이동
- https://hub.docker.com/r/jenkins/jenkins 

* 이미지 다운로드
```
docker pull jenkins/jenkins
```

2. Jenkins 실행
port 변경(컨테이너 외부 호출 : 컨테이너 내부 호출), name(이름 설정, 설정안하는 경우 임의 생성), restart(fail이라면 restart)
-d(터미널 사용을 위해 백그라운드 데몬 형태로 실행)

```
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins-server --restart=on-failure jenkins/jenkins:lts-jdk11
```

3. Jenkins 초기 접속
http://127.0.0.1:8080
Administrator password

* 컨테이너 내 파일 확인
Docker 컨테이너에 직접 접속해서 파일을 확인할 수도 있다
도커가 설치된 경로 (윈도우)
```
C:\WINDOWS\system32>docker exec jenkins-server cat /var/jenkins_home/secrets/initialAdminPassword
```

- - -


# 도커 명령어

```
docker ps
docker container exec -it 'docker container id를 입력' bash
```

![image](https://user-images.githubusercontent.com/47144594/229289296-2bc907ee-9594-4e01-9e98-9f47278e5296.png)

- - -

# git 설정
- git 저장소 확인
- branch 이름 확인
![image](https://user-images.githubusercontent.com/47144594/229289097-fadb54a3-eb6c-4dfa-9f4d-f8e090f34949.png)


# 배포 설정
- ip 주소는 변경될 수 있으므로 확인할 것.
- 127.0.0.1 이 아닌 WAS(tomcat)이 있는 서버의 아이피
![image](https://user-images.githubusercontent.com/47144594/229289048-8c0fcad4-f3a3-43d1-be9e-8d159ae006d4.png)

# 자동 빌드
- 스케줄러에 따라 git에서 변경사항이 있는 경우 빌드 및 배포
![image](https://user-images.githubusercontent.com/47144594/229289142-2d518bc3-0e73-4526-b6a6-f9dd4a8a8ae4.png)

# 빌드 방식
- clean, complile, package
![image](https://user-images.githubusercontent.com/47144594/229289177-ac911690-960b-4c79-9b20-2a1b9d765419.png)

- - -

# pipeline
- plugin : delivery pipeline
- 각각의 job에서 빌드 후 조치 : Build other projects > Trigger only if build is stable


# Delivery Pipeline (View DashBoard)

 (1) My Views 라는 메뉴가 생성된다.
![image](https://user-images.githubusercontent.com/47144594/229983172-4c30e3d2-b9ae-4a79-b9f7-9bef45b9bb33.png)

 (2) 새로운 View 추가 및 설정
 - pipeline component : 이름 설정, 초기 실행 JOB 설정을 할 수 있다. 
![image](https://user-images.githubusercontent.com/47144594/229983228-f5827b45-bda9-4367-9646-07461c659dca.png)

 (3) 생성된 View 확인
 ![image](https://user-images.githubusercontent.com/47144594/229983329-c808aa05-b01a-4fd3-af14-55f0e1451b1b.png)

# pipe-line Script 작성하기

```
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
```

# pipeline Git에서 Script 가져와서 실행하기
1. Pipeline project 생성 및 Pipeline Syntax
  (1) item 생성 >Pipeline (project) > 하단 Pipeline scirpt > Pipeline Syntax
  (2) Steps > git: Git 선택 > Repository, Branch, 입력 & Generate Pipeline Script
      -> 생성된 git command를 다음에 복사
![image](https://user-images.githubusercontent.com/47144594/229342278-f1279433-b3ef-4f4a-a4dd-940ee85011d9.png)

2. 생성하던 프로젝트 설정으로 돌아와서 스크립트를 넣어준다.
![image](https://user-images.githubusercontent.com/47144594/229342350-ead88e2f-2427-41e0-8562-07b589b05a71.png)

# Pipeline Dash board (Stage view)

- stages에 설정한 대로 stage view 에 노출이 된다.

```
pipeline {
    agent any
    stages {
        stage('Compile') {
            steps {
                echo "Compiled successfully!";
            }
        }

        stage('JUnit') {
            steps {
                echo "JUnit passed successfully!";
            }
        }

        stage('Code Analysis') {
            steps {
                echo "Code Analysis completed successfully!";
            }
        }

        stage('Deploy') {
            steps {
                echo "Deployed successfully!";
            }
        }
    }

    post {
      always {
        echo "This will always run"
      }
      success {
        echo "This will run when the run finished successfully"
      }
      failure {
        echo "This will run if failed"
      }
      unstable {
        echo "This will run when the run was marked as unstable"
      }
      changed {
        echo "This will run when the state of the pipeline has changed"
      }
    }
}
```

![image](https://user-images.githubusercontent.com/47144594/229356342-0cd64d10-0da2-4605-80cf-e3d0c5eb6e1a.png)


- - -

# 권한 문제
- 스크립트에 의한 파일 실행 권한이 없으므로 파일을 실행할때 권한 문제가 발생된다.

## 1. 에러
-  ./pipelineScript/build.sh: Permission denied 권한이 없다는 에러가 발생
![image](https://user-images.githubusercontent.com/47144594/229343710-b41dd5dc-9c37-4a5a-92c3-d540c1c140ca.png)

## 2. 권한 확인
서버에서 확인해보니 해당 파일에 실행권한이 없었다.

```
경로 : /var/jenkins_home/workspace/My-Second-Pipeline
파일 : .sh
```

![image](https://user-images.githubusercontent.com/47144594/229343745-de6047d1-36b9-48fa-9831-a89a00041a9d.png)

## 3. 권한 부여
- 해당 파일이 있는 경로에서 git 명령어 실행

```
    git update-index --add --chmod=+x build.sh
    git update-index --add --chmod=+x deploy.sh
    git update-index --add --chmod=+x quality.sh
    git update-index --add --chmod=+x unit.sh
    git commit -m "Make build.sh executable" 
    git push -u origin master
```

(참고 : https://stackoverflow.com/questions/42154912/permission-denied-for-build-sh-file)
![image](https://user-images.githubusercontent.com/47144594/229343805-9717fe79-350c-4d1c-9491-aac5deda8bcc.png)

## 4. Pipeline project 에서 '지금 빌드' 실행

## 5. 권한 재확인
 - 권한은 정상적으로 부여되고 실행도 정상적으로 실행된다.
![image](https://user-images.githubusercontent.com/47144594/229343909-19717ab6-f831-4851-b8ae-c5a001082ad0.png)


# Sciprt (maven build)
```
pipeline {
    agent any
    tools { 
      maven 'Maven3.8.5' // Jenkins > manage > configureTools 에서 Maven 항목을 열어보면 버전을 확인할 수 있다.
    }
    stages {
        stage('github clone') {
            steps {                
                git 'https://github.com/amirer21/cicd-project' // 해당 items에서 > Configure > 하단에 Pipeline Syntax > Step항목 Git Repository, branch를 넣고 Generate
            }
        }
        
        stage('build') {
            steps {
                sh '''
                    echo build start
                    mvn clean compile package -DskipTests=true
                '''
            }
        }
    }
}
```
