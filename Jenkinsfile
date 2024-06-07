pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Установка зависимостей из файла requirements.txt
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Python Scripts') {
            steps {
                script {
                    echo 'Running Python scripts...'

                    sh 'python3 scripts/main.py'
                    echo 'Finished running scripts'

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