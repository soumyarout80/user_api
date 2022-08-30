
#!groovy

//Groovy pipeline code


pipeline {
    agent any
    stages{

        stage('Checkout') {
            steps {
            deleteDir()
            // Get  code from a git repository
            sh """
            git clone https://github.com/soumyarout80/user_api.git
            """
            }
        }

        stage('Build & unittest') {
            steps {
            // Unit testing for all methods
            dir("work_directory"){
            sh """
            pip3 install -r requirements.txt
            flake8 --extend-ignore E501,E125,E501
            python3 -m unittest -v user_api
            pytest --cov=user_api --cov-report=xml --cov-branch
            """
            }
               }
        }

        stage('Deployment to local system') {
            steps {
            // Unit testing
            dir("work_directory"){
            sh """
            pip install gunicorn
            gunicorn wsgi -b 127.0.0.1:8000 --pid /tmp/gunicorn.pid --daemon
            """
            }
                }
        }

        stage("BDT report generation") {
            steps {
            // User report creation
            dir("work_directory"){
            sh """
            behave --no-capture --format plain
            """
            }
          }
        }

    }
}