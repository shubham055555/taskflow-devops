pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Dependencies') {
            steps {
                sh '''
                    python3 -m pip --version

                    python3 -m pip install \
                        --user \
                        --break-system-packages \
                        -r backend/requirements.txt \
                        pytest
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