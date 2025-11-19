pipeline {
  agent any

  environment {
    DOCKER_IMAGE = "YOUR_DOCKERHUB_USERNAME/devops-flask-demo"
    DOCKER_TAG = "${env.BUILD_NUMBER}"
    DOCKER_HUB_CREDENTIALS = 'docker-hub-creds' // change if you use different ID
    DEPLOY_CONTAINER_NAME = "devops-flask-demo"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ./app"
          sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest"
        }
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: env.DOCKER_HUB_CREDENTIALS, usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
          sh "echo $DH_PASS | docker login -u $DH_USER --password-stdin"
          sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
          sh "docker push ${DOCKER_IMAGE}:latest"
          sh "docker logout"
        }
      }
    }

    stage('Deploy') {
      steps {
        // Simple deploy: stop and remove old container and run new one
        script {
          sh """
            if [ \$(docker ps -aq -f name=${DEPLOY_CONTAINER_NAME}) ]; then
              docker rm -f ${DEPLOY_CONTAINER_NAME} || true
            fi
            docker run -d --name ${DEPLOY_CONTAINER_NAME} -p 5000:5000 \\
              -e APP_NAME=DevOpsDemo -e APP_VERSION=${DOCKER_TAG} ${DOCKER_IMAGE}:${DOCKER_TAG}
          """
        }
      }
    }
  }

  post {
    always {
      echo "Pipeline finished. Image: ${DOCKER_IMAGE}:${DOCKER_TAG}"
    }
  }
}
