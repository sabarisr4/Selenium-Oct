pipeline {
    agent any

    options {
        timestamps()
        skipDefaultCheckout(true)
    }

    environment {
        VENV = '.venv'
        PYTHONUNBUFFERED = '1'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning GitHub repository...'
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv ${VENV}
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python -m pip install --upgrade pip

                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        pip install pytest selenium
                    fi
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate

                    if [ -d Pytest ]; then
                        TEST_DIR=Pytest
                    else
                        TEST_DIR=.
                    fi

                    pytest "$TEST_DIR" -v \
                        --junitxml=pytest-results.xml
                '''
            }
        }
    }

    post {
        always {
            junit(
                testResults: 'pytest-results.xml',
                allowEmptyResults: true
            )

            archiveArtifacts(
                artifacts: 'pytest-results.xml',
                allowEmptyArchive: true
            )
        }

        success {
            echo 'Selenium tests completed successfully!'
        }

        failure {
            echo 'Selenium tests failed. Check Console Output.'
        }
    }
}