pipeline {
    agent any
    environment {
        PYTHON_PATH = 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python313\\Scripts'
    }
    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }
        stage("Build") {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip install -r requirements.txt
                '''
            }
        }
        stage("Sonar-Analysis") {
            environment {
                SONAR_TOKEN = credentials('sonar-token')
            }
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner -Dsonar.projectKey=task8sonar ^
                -Dsonar.sources=. ^
                -Dsonar.host.url=http://localhost:9000 ^
                -Dsonar.token=%SONAR_TOKEN%
                '''
            }
        }
    }
    post {
        success {
            echo "went well and good"
        }
        failure {
            echo "failed"
        }
    }
}
