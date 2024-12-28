pipeline{
    agent any 
    environment{
        PYTHON_PATH = "C:\\Users\\sheik\\AppData\\Local\\Programs\\Python\\Python311;C:\\Users\\sheik\\AppData\\Local\\Programs\\Python\\Python311\\Scripts"
    }
    stages{
        stage('Checkout'){
            steps{
                checkout scm
            }
        }
        stage('Build'){
            steps{
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner --version

                pip install pytest pytest-cov coverage
                '''
            }
        }
        stage('SonarAnalysis'){
            environment{
                SONAR_TOKEN=credentials('sonarqube-token')
            }
            steps{
                bat '''
                set PATH=%PYTHON_PATH%;%PATH% 
                sonar-scanner -Dsonar.sources=. ^
                -Dsonar.python.version=3.x ^
                -Dsonar.language=python ^
                -Dsonar.projectKey=project-with-coverage ^
                -Dsonar.tests=. ^
                -Dsonar.test.inclusions=test_*.py ^
                -Dsonar.python.xunit.reportPath=test-reports/pytest-report.xml ^
                -Dsonar.python.coverage.reportPaths=coverage.xml ^
                -Dsonar.coverage.exclusions=test_*.py ^
                -Dsonar.host.url=http://localhost:9000 ^
                -Dsonar.sourceEncoding=UTF-8 ^
                '''
            }
        }
    }
    post{
        success{
            echo "DONE SUCCESSFULLY"
        }
        failure{
            echo "SOMETHING IS WRONG"
        }
    }
    
}
