pipeline {
    agent any

    triggers {
        githubPush()              // Auto-run pipeline whenever code is pushed
        //pollSCM('H/2 * * * *')   // Optional: Run every 2 mins even if webhook fails
    }

    environment {
        DH_USER = 'rahul3mukhe0405'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                bat 'echo Running tests...'
                bat 'python -m pip install -r app/requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DH_USER%/devops-flask-demo:%BUILD_NUMBER% ./app"
                bat "docker tag %DH_USER%/devops-flask-demo:%BUILD_NUMBER% %DH_USER%/devops-flask-demo:latest"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DH_USER_VAR',
                    passwordVariable: 'DH_PASS'
                )]) {
                    bat "echo %DH_PASS% | docker login -u %DH_USER_VAR% --password-stdin"
                    bat "docker push %DH_USER%/devops-flask-demo:%BUILD_NUMBER%"
                    bat "docker push %DH_USER%/devops-flask-demo:latest"
                    bat "docker logout"
                }
            }
        }

        stage('Deploy') {
            steps {
                bat "docker rm -f devops-flask-demo || echo no old container"
                bat "docker run -d --name devops-flask-demo -p 5000:5000 %DH_USER%/devops-flask-demo:%BUILD_NUMBER%"
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
    }
}
