pipeline {
    agent any

    stages {

        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Setup Python Environment") {
            steps {
                sh "python3 -m venv .venv"
                sh ".venv/bin/python -m pip install --upgrade pip"
                sh ".venv/bin/python -m pip install -r backend/requirements.txt"
                sh ".venv/bin/python -m pip install pytest"
            }
        }

        stage("Run Tests") {
            steps {
                sh ".venv/bin/python -m pytest -v"
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