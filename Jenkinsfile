pipeline {
    agent any

    environment {
        SRC_DIR  = 'devops-project/myweb'
        DEST_DIR = '/var/www/html'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Static files hain, koi build step nahi chahiye.'
                sh "ls -la ${SRC_DIR}"
            }
        }

        stage('Test') {
            steps {
                script {
                    // Basic sanity check - index.html file exist karta hai ya nahi
                    def indexExists = sh(script: "test -f ${SRC_DIR}/index.html", returnStatus: true)
                    if (indexExists != 0) {
                        error("Test Failed: index.html nahi mila ${SRC_DIR} mein")
                    } else {
                        echo 'Test Passed: index.html mil gaya.'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                sh """
                    sudo cp -r ${SRC_DIR}/* ${DEST_DIR}/
                    sudo systemctl restart apache2 || sudo systemctl restart httpd
                """
            }
        }
    }

    post {
        success {
            echo '✅ Deploy successful — website live on EC2.'
        }
        failure {
            echo '❌ Pipeline fail ho gaya, logs check karo.'
        }
    }
}
