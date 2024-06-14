pipeline {
    agent any

    stages {
        stage('Start') {
            steps {
                script {
                    echo 'Начало работы скриптов.'
                }
            }
        }

        stage('Preparation') {
            steps {
                // Очистка рабочего пространства
                cleanWs()
                checkout scm
            }
        }

        stage('Checkout') {
            steps {
                script {
                    // Получаем исходный код из репозитория Git
                    git branch: 'jenkins-and-tests', url: 'https://github.com/kcherenkovv/MLOps_project'
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                // Создание виртуального окружения
                script {
                    if (isUnix()) {
                        sh 'python -m venv venv'
                    } else {
                        bat 'python -m venv venv'
                    }
                }
            }
        }

        stage('Activate venv') {
            steps {
                // Активация виртуального окружения
                script {
                    if (isUnix()) {
                        sh './venv/scripts/activate.bat'
                    } else {
                        bat '.\\venv\\scripts\\activate.bat'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                // установка зависимостей
                script {
                    if (isUnix()) {
                        sh 'pip install -r requirements.txt'
                    } else {
                        bat 'pip install -r requirements.txt'
                    }
                }
            }
        }

         stage('Run Unit Tests') {
            steps {
                // установка зависимостей
                script {
                    if (isUnix()) {
                        sh 'pytest'
                    } else {
                        bat 'pytest'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}