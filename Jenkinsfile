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
                sh 'python3 --version'
                sh '''
                    python3 -c 'import flask, flask_sqlalchemy, flask_cors, pytest; print("Dependencies OK")'
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    PYTHONPATH=backend python3 -m pytest -v
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                    echo "TaskFlow build completed successfully"
                '''
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