pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    docker run --rm \
                      -v "$PWD:/workspace" \
                      -w /workspace \
                      python:3.13-slim \
                      sh -c "pip install --no-cache-dir -r backend/requirements.txt && pip install --no-cache-dir pytest"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm \
                      -v "$PWD:/workspace" \
                      -w /workspace \
                      python:3.13-slim \
                      sh -c "pip install --no-cache-dir -r backend/requirements.txt pytest && PYTHONPATH=backend pytest -v"
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