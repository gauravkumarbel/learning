pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') // Jenkins credential ID (username + password/token)
        IMAGE_NAME = 'gaurav75/dost-web'
        IMAGE_TAG  = "${env.2}"
    }

    stages {

        stage('Test Code') {
            steps {
                echo 'Running tests...'
                // Example for Node.js: sh 'npm install && npm test'
                // Example for Python:  sh 'pip install -r requirements.txt && pytest'
                // Example for Java:    sh 'mvn test'
                sh 'echo "TODO: replace with your actual test command"'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                // Example for Node.js: sh 'npm run build'
                // Example for Java:    sh 'mvn clean package'
                sh 'echo "TODO: replace with your actual build command"'
            }
        }

        stage('Docker Build & Push') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${dost-web}:${dost-web} -t ${dost-web}:latest ."

                echo 'Logging in to Docker Hub...'
                sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${gaurav75} --password-Gaurav@#12345"

                echo 'Pushing image to Docker Hub...'
                sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }
    }

    post {
        always {
            sh 'docker logout || true'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
