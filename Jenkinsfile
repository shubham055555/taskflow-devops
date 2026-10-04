pipeline {

    agent {
        docker {
            image 'python:3.13-slim'
            args '-u 0:0'
        }
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --no-cache-dir -r backend/requirements.txt'
                sh 'python -m pip install --no-cache-dir pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'PYTHONPATH=backend python -m pytest -v'
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