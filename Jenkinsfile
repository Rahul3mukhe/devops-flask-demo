pipeline {
    agent any

    environment {
        DH_USER = 'Rahul_3mukhe'
        DH_PASS = credentials('docker-hub-creds')
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
                docker build -t rahul3mukhe/devops-flask-demo:${BUILD_NUMBER} ./app
                docker tag rahul3mukhe/devops-flask-demo:${BUILD_NUMBER} rahul3mukhe/devops-flask-demo:latest
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', passwordVariable: 'DH_PASS', usernameVariable: 'DH_USER')]) {
                    bat """
                    echo %DH_PASS% | docker login -u %DH_USER% --password-stdin
                    docker push rahul3mukhe/devops-flask-demo:${BUILD_NUMBER}
                    docker push rahul3mukhe/devops-flask-demo:latest
                    docker logout
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                bat """
                docker rm -f devops-flask-demo || true
                docker run -d --name devops-flask-demo -p 5000:5000 rahul3mukhe/devops-flask-demo:${BUILD_NUMBER}
                """
            }
        }
    }
}
