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
                    python3 /tmp/get-pip.py --break-system-packages
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

        stage('SonarQube Analysis') {
            steps {
                echo 'SonarQube stage completed for this lab'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    echo "TaskFlow build completed successfully"
                '''
            }
        }

        stage('Kubernetes Diagnostics') {
    steps {
        sh '''
            echo "=== Kubernetes server used by Jenkins ==="
            kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
            echo
            echo "=== Kubernetes context ==="
            kubectl config current-context
            echo
            echo "=== Kubeconfig location ==="
            echo \
            echo
        '''
    }
}

stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    echo "Checking Kubernetes access..."
                    kubectl version --client

                    echo "Applying Kubernetes manifests..."
                    kubectl apply -f k8s/configmap.yaml
                    kubectl apply -f k8s/secret.yaml
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml

                    echo "Waiting for Kubernetes rollout..."
                    kubectl rollout status deployment/taskflow --timeout=120s
                '''
            }
        }

        stage('Verify Kubernetes Deployment') {
            steps {
                sh '''
                    echo "Kubernetes Deployment:"
                    kubectl get deployment taskflow

                    echo "Kubernetes Pods:"
                    kubectl get pods -l app=taskflow

                    echo "Kubernetes Service:"
                    kubectl get service taskflow-service
                '''
            }
        }
    }

    post {
        success {
            echo 'TaskFlow CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'TaskFlow CI/CD Pipeline failed!'
        }
    }
}

