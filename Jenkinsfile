
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\sabar\\AppData\\Local\\Python\\pythoncore-3.15-64\\python.exe'
    }

    options {
        timestamps()
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat '''
                    "%PYTHON%" --version
                    "%PYTHON%" -m pip --version
                    "%PYTHON%" -m venv .venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
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
                    echo 'No test report generated.'
                }
            }
        }

        success {
            echo 'Python Selenium pipeline completed!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
