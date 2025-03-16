pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "rsrs88/jenkins"
        DOCKER_TAG = "latest"
        REGISTRY_CREDENTIALS = 'docker-hub-credentials'  // Jenkins credentials ID
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/raz-project/jenkins2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $DOCKER_IMAGE:$DOCKER_TAG ."
                }
            }
        }

        stage('Tag Docker Image') {
            steps {
                script {
                    sh "docker tag $DOCKER_IMAGE:$DOCKER_TAG $DOCKER_IMAGE:$BUILD_NUMBER"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withDockerRegistry([credentialsId: REGISTRY_CREDENTIALS, url: '']) {
                        sh "docker push $DOCKER_IMAGE:$DOCKER_TAG"
                        sh "docker push $DOCKER_IMAGE:$BUILD_NUMBER"
                    }
                }
            }
        }
    }
}
