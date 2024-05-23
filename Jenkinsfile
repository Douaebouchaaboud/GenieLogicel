pipeline {
    agent any

    environment {
        // Environment variables can be defined here
        PYTHON_ENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Douaebouchaaboud/GenieLogicel'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv ${PYTHON_ENV}
                source ${PYTHON_ENV}/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                source ${PYTHON_ENV}/bin/activate
                flake8 .
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                source ${PYTHON_ENV}/bin/activate
                python manage.py test
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage - define your deployment steps here'
               
            }
        }
    }

    post {
        always {
            cleanWs()
        }

        success {
            echo 'Pipeline succeeded!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
