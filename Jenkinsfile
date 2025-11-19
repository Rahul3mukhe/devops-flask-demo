pipeline {
    agent any

    environment {
        DH_USER = 'rahul3mukhe0405'
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
                    docker build -t %DH_USER%/devops-flask-demo:%BUILD_NUMBER% ./app
                    docker tag %DH_USER%/devops-flask-demo:%BUILD_NUMBER% %DH_USER%/devops-flask-demo:latest
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-creds',
                    usernameVariable: 'DH_USER_VAR',
                    passwordVariable: 'DH_PASS'
                )]) {
                    bat """
                        echo Logging in to Docker Hub...
                        echo %DH_PASS% | docker login -u %DH_USER_VAR% --password-stdin

                        echo Pushing image...
                        docker push %DH_USER%/devops-flask-demo:%BUILD_NUMBER%
                        docker push %DH_USER%/devops-flask-demo:latest

                        docker logout
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                bat """
                    echo Stopping old container...
                    docker rm -f devops-flask-demo || echo No old container

                    echo Running new container...
                    docker run -d --name devops-flask-demo -p 5000:5000 %DH_USER%/devops-flask-demo:%BUILD_NUMBER%
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
