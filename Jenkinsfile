pipeline {
    agent any

    stages {

        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Diagnose Python") {
            steps {
                sh "which python3 || true"
                sh "python3 --version || true"
                sh "python3 -m pip --version || true"
                sh "ls -la /usr/bin/python3 || true"
                sh "ls -la /opt || true"
            }
        }

        stage("Install Dependencies") {
            steps {
                sh "python3 -m pip install -r backend/requirements.txt"
            }
        }

        stage("Run Tests") {
            steps {
                sh "python3 -m pytest -v"
            }
        }

        stage("Build") {
            steps {
                sh "echo 'TaskFlow build completed successfully'"
            }
        }
    }

    post {
        success {
            echo "TaskFlow CI Pipeline completed successfully!"
        }

        failure {
            echo "TaskFlow CI Pipeline failed!"
        }
    }
}