pipeline {
    agent any

    environment {
        DOCKER_USER = 'rahul3mukhe0405'
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
                    echo Building Docker Image...
                    docker build -t %DOCKER_USER%/devops-flask-demo:%BUILD_NUMBER% ./app
                    docker tag %DOCKER_USER%/devops-flask-demo:%BUILD_NUMBER% %DOCKER_USER%/devops-flask-demo:latest
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'LOGIN_USER',
                    passwordVariable: 'LOGIN_PASS'
                )]) {

                    bat """
                        echo Logging in to Docker Hub...
                        echo %LOGIN_PASS% | docker login -u %LOGIN_USER% --password-stdin

                        echo Pushing images...
                        docker push %DOCKER_USER%/devops-flask-demo:%BUILD_NUMBER%
                        docker push %DOCKER_USER%/devops-flask-demo:latest

                        docker logout
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                bat """
                    echo Stopping old container...
                    docker rm -f devops-flask-demo || echo No old container found

                    echo Running new container...
                    docker run -d --name devops-flask-demo -p 5000:5000 %DOCKER_USER%/devops-flask-demo:%BUILD_NUMBER%
                """
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
    }
}
