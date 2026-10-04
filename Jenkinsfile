pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install pip') {
            steps {
                sh '''
                    python3 --version

                    curl -sS https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py

                    python3 /tmp/get-pip.py \
                        --break-system-packages

                    python3 -m pip --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install \
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