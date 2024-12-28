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
                sonar-scanner sonar.sources=.
                sonar.python.version=3.x
                sonar.language=python
                sonar.projectKey=project-with-coverage


                # Tests
                sonar.tests=.
                sonar.test.inclusions=test_*.py
                sonar.python.xunit.reportPath=test-reports/pytest-report.xml

                # Coverage
                sonar.python.coverage.reportPaths=coverage.xml
                sonar.coverage.exclusions=test_*.py

                # Other settings
                sonar.host.url=http://localhost:9000
                sonar.sourceEncoding=UTF-8
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
