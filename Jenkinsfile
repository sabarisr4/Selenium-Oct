
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
                echo 'Downloading GitHub repository...'
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
<<<<<<< HEAD
                bat 'python --version'
                bat 'python -m pip --version'
                bat 'python -m venv .venv'
=======
                bat '''
                    "%PYTHON%" --version
                    "%PYTHON%" -m pip --version
                    "%PYTHON%" -m venv .venv
                '''
>>>>>>> 7fa5b7c (Configure Python executable for Jenkins)
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
<<<<<<< HEAD

                    if exist requirements.txt (
                        .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                    ) else (
                        .venv\\Scripts\\python.exe -m pip install pytest selenium
                    )
=======
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
>>>>>>> 7fa5b7c (Configure Python executable for Jenkins)
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
<<<<<<< HEAD
                    echo 'No Pytest XML report was generated.'
                }
            }

            archiveArtifacts(
                artifacts: 'pytest-results.xml',
                allowEmptyArchive: true
            )
=======
                    echo 'No test report generated.'
                }
            }
>>>>>>> 7fa5b7c (Configure Python executable for Jenkins)
        }

        success {
            echo 'Python Selenium pipeline completed!'
        }

        failure {
<<<<<<< HEAD
            echo 'Build failed. Check Console Output.'
=======
            echo 'Pipeline failed. Check Console Output.'
>>>>>>> 7fa5b7c (Configure Python executable for Jenkins)
        }
    }
}
