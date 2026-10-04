pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Environment Check') {
            steps {
                sh '/opt/taskflow-venv/bin/python --version'
                sh '/opt/taskflow-venv/bin/python -c "import flask, flask_sqlalchemy, flask_cors, pytest; print(\"Dependencies OK\")"'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'PYTHONPATH=backend /opt/taskflow-venv/bin/python -m pytest -v'
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