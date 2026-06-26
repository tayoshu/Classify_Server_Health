pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Administrator\\AppData\\Roaming\\uv\\python\\cpython-3.13.5-windows-x86_64-none\\python.exe" -m pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\Administrator\\AppData\\Roaming\\uv\\python\\cpython-3.13.5-windows-x86_64-none\\python.exe" -m pytest tests/ -v --tb=short'
            }
        }

        stage('Coverage Report') {
            steps {
                bat '"C:\\Users\\Administrator\\AppData\\Roaming\\uv\\python\\cpython-3.13.5-windows-x86_64-none\\python.exe" -m pytest tests/ --cov=src --cov-report=term-missing'
            }
        }
    }

    post {
        success {
            echo 'All tests passed. Component is healthy.'
        }
        failure {
            echo 'Tests failed. Review the output above to identify the problem.'
        }
    }
}
