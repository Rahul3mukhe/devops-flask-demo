pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "Rahul_3mukhe/devops-flask-demo"
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        DOCKER_HUB_CREDENTIALS = 'docker-hub-creds'
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
                bat """
                docker build -t %DOCKER_IMAGE%:%DOCKER_TAG% ./app
                docker tag %DOCKER_IMAGE%:%DOCKER_TAG% %DOCKER_IMAGE%:latest
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: env.DOCKER_HUB_CREDENTIALS, usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                    bat """
                    echo %DH_PASS% | docker login -u %DH_USER% --password-stdin
                    docker push %DOCKER_IMAGE%:%DOCKER_TAG%
                    docker push %DOCKER_IMAGE%:latest
                    docker logout
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                bat """
                docker rm -f %DEPLOY_CONTAINER_NAME% || true
                docker run -d --name %DEPLOY_CONTAINER_NAME% -p 5000:5000 %DOCKER_IMAGE%:%DOCKER_TAG%
                """
            }
        }
    }

    post {
        always {
            echo "Pipeline finished successfully."
        }
    }
}
