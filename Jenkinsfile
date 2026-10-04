pipeline {
    agent any

    stages {
        stage('Docker Diagnostic') {
            steps {
                sh 'id'
                sh 'ls -ln /var/run/docker.sock'
                sh 'docker version'
                sh 'docker ps'
            }
        }
    }
}