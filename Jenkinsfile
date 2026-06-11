pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/employee-management.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Code Quality Check') {
            steps {
                bat 'venv\\Scripts\\pylint app.py'
            }
        }

        stage('Unit Testing') {
            steps {
                bat 'venv\\Scripts\\pytest'
            }
        }

        stage('Build') {
            steps {
                echo 'Build artifact generated successfully'
            }
        }

        stage('Success Notification') {
            steps {
                echo 'Employee Management API build successful'
            }
        }
    }
}