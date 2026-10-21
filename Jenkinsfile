pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'if not exist index.html exit /b 1'
                bat 'if not exist style.css exit /b 1'
                bat 'if not exist script.js exit /b 1'
                bat 'if not exist test.py exit /b 1'
                bat 'echo Build completed successfully'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\pakash chandra shukl\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" test.py'
            }
        }
    }

    post {
        success {
            echo 'Build and tests completed successfully!'
        }
        failure {
            echo 'Build or tests failed. Check the console output.'
        }
    }
}
