pipeline {
    agent any

    stages {

        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Install Dependencies") {
            steps {
                sh "python -m pip install -r backend/requirements.txt"
            }
        }

        stage("Run Tests") {
            steps {
                sh "python -m pytest -v"
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