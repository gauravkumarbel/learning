pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'ls -la'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
    }
}
