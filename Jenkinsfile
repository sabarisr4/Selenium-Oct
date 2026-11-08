
pipeline {
    agent any

    options {
        timestamps()
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Downloading GitHub repository...'
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
                bat 'python -m pip --version'
                bat 'python -m venv .venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    .venv\\Scripts\\python.exe -m pip install --upgrade pip

                    if exist requirements.txt (
                        .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                    ) else (
                        .venv\\Scripts\\python.exe -m pip install pytest selenium
                    )
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '''
                    if exist Pytest (
                        .venv\\Scripts\\python.exe -m pytest Pytest -v --junitxml=pytest-results.xml
                    ) else (
                        .venv\\Scripts\\python.exe -m pytest . -v --junitxml=pytest-results.xml
                    )
                '''
            }
        }
    }

    post {
        always {
            script {
                if (fileExists('pytest-results.xml')) {
                    junit testResults: 'pytest-results.xml',
                          allowEmptyResults: true
                } else {
                    echo 'No Pytest XML report was generated.'
                }
            }

            archiveArtifacts(
                artifacts: 'pytest-results.xml',
                allowEmptyArchive: true
            )
        }

        success {
            echo 'Selenium tests completed successfully!'
        }

        failure {
            echo 'Build failed. Check Console Output.'
        }
    }
}
