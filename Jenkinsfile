pipeline {
    agent any

    stages {

        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Diagnose Jenkins Environment") {
            steps {
                sh "id"
                sh "pwd"
                sh "ls -la /opt/taskflow-venv/bin/python"
                sh "ls -la /opt/taskflow-venv/bin/python3"
                sh "/opt/taskflow-venv/bin/python --version"
                sh "/opt/taskflow-venv/bin/python -m pip --version"
            }
        }

        stage("Install Dependencies") {
            steps {
                sh "/opt/taskflow-venv/bin/python -m pip install -r backend/requirements.txt"
            }
        }

        stage("Run Tests") {
            steps {
                sh "/opt/taskflow-venv/bin/python -m pytest -v"
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