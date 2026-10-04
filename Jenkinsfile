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
                sh "python3 -m pip install --upgrade pip"
                sh "pip3 install -r backend/requirements.txt"
                sh "pip3 install pytest"
            }
        }

        stage("Run Tests") {
            steps {
                sh "PYTHONPATH=backend pytest -v"
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
