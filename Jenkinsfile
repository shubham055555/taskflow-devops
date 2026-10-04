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
                bat "python -m pip install --upgrade pip"
                bat "pip install -r backend/requirements.txt"
                bat "pip install pytest"
            }
        }

        stage("Run Tests") {
            steps {
                bat "set PYTHONPATH=backend&& pytest -v"
            }
        }

        stage("Build") {
            steps {
                echo "Build completed successfully"
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
