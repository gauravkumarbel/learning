pipeline {
    agent any

    environment {
        TARGET_PATH = 'devops-project/myweb'   // sirf isi folder/file ko target karenge
        TARGET_FILE = 'index.html'             // jo html file test karni hai
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm   // poora repo aayega, but hum sirf TARGET_PATH use karenge
            }
        }

        stage('Verify File Exists') {
            steps {
                script {
                    def exists = fileExists "${TARGET_PATH}/${TARGET_FILE}"
                    if (!exists) {
                        error("❌ ${TARGET_FILE} nahi mila ${TARGET_PATH} mein")
                    } else {
                        echo "✅ File mil gaya: ${TARGET_PATH}/${TARGET_FILE}"
                    }
                }
            }
        }

        stage('Build (HTML Validation)') {
            steps {
                dir("${TARGET_PATH}") {
                    sh """
                        # HTML syntax check ke liye tidy tool use karo
                        which tidy || sudo apt-get install -y tidy
                        tidy -q -e ${TARGET_FILE} || echo "⚠️ Warnings mile, but continue kar rahe hain"
                    """
                }
            }
        }

        stage('Test') {
            steps {
                dir("${TARGET_PATH}") {
                    script {
                        def content = readFile("${TARGET_FILE}")
                        if (!content.contains('<html')) {
                            error("❌ Test Failed: valid HTML tag nahi mila")
                        } else {
                            echo "✅ Test Passed: valid HTML structure hai"
                        }
                    }
                }
            }
        }
    }

    post {
        success {
            echo "🎉 Build & Test successful for ${TARGET_PATH}/${TARGET_FILE}"
        }
        failure {
            echo "🚫 Pipeline failed — check logs above"
        }
    }
}
