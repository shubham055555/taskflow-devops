pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv .ci-venv
                    .ci-venv/bin/python -m pip install --upgrade pip
                    .ci-venv/bin/pip install -r backend/requirements.txt
                    .ci-venv/bin/pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    PYTHONPATH=backend .ci-venv/bin/python -m pytest -v
                '''
            }
        }

        stage('Build') {
            steps {
                sh "echo 'TaskFlow build completed successfully'"
            }
        }
    }

    post {

        success {
            echo 'TaskFlow CI Pipeline completed successfully!'
        }

        failure {
            echo 'TaskFlow CI Pipeline failed!'
        }
    }
}