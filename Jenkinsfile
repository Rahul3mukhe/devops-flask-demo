pipeline {
    agent any

    environment {
        DH_USER = 'rahul3mukhe0405'
    }

    triggers {
        githubPush()        // AUTO trigger when code is updated
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    echo Running basic test...
                    python --version
                    echo "New test line added"
                    echo "Test line 2 added"
                    echo "Sir, this is automatic update test"


                """
                

            }
        }

        stage('Build Docker Image') {
            steps {
                bat """
                    echo Building Docker image...
                    docker build -t %DH_USER%/devops-flask-demo:%BUILD_NUMBER% ./app
                    docker tag %DH_USER%/devops-flask-demo:%BUILD_NUMBER% %DH_USER%/devops-flask-demo:latest
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DH_USER_VAR',
                    passwordVariable: 'DH_PASS')])
                {
                    bat """
                        echo Logging in...
                        echo %DH_PASS% | docker login -u %DH_USER_VAR% --password-stdin

                        echo Pushing images...
                        docker push %DH_USER%/devops-flask-demo:%BUILD_NUMBER%
                        docker push %DH_USER%/devops-flask-demo:latest
                    """
                }
            }
        }

        stage('Blue-Green Deploy') {
            steps {
                bat """
                    echo Removing previous container...
                    docker rm -f devops-flask-demo || echo no-old-container

                    echo Starting new version...
                    docker run -d --name devops-flask-demo -p 5000:5000 %DH_USER%/devops-flask-demo:%BUILD_NUMBER%
                """
            }
        }
    }

    post {
        success {
            emailext(
                to: "yourmail@gmail.com",
                subject: "Deployment Successful: Build #${BUILD_NUMBER}",
                body: "Your Flask app has been successfully deployed.\n\nTag: ${BUILD_NUMBER}"
            )
        }
        failure {
            emailext(
                to: "yourmail@gmail.com",
                subject: "Deployment FAILED: Build #${BUILD_NUMBER}",
                body: "Deployment failed. Please check Jenkins logs."
            )
        }
    }
}