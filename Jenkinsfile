pipeline {
    
    agent any

      environment {
        docker_cred = credentials('docker_credential')
    
    }

    stages {
        stage('fetch_code') {
            steps {
                git branch : 'main',url : "https://github.com/rahulshri0703/app100.git"
            }
        post {
            success {
                echo "pulled succesful"
                archiveArtifacts  artifacts: "**/*.py"  
              
            }
        }
        }

        stage('echo') {
            steps {
                sh "echo GOOD"
                sh "pwd"
            }
        }

     stage('Login to DOCKER') {
            steps {
                // login to docker
                 sh "echo $docker_cred_PSW | docker login -u $docker_cred_USR --password-stdin"
}
}

          stage('BUILDING DOCKER IMAGE') {
            steps {
                sh "ls"
                sh "docker build -t rahulshri0703/app100_version:$BUILD_NUMBER -t rahulshri0703/app100_version:latest ."
                // sh "docker tag new999:$BUILD_NUMBER rahulshri0703/new999:$BUILD_NUMBER"
            }
        
        }

        // create a docker_credentials in Dashboard>Manage Jenkins>Credentials>System>Global credentials (unrestricted)

               stage('push to DOCKER') {
            steps {
               
                // push 
                sh "docker push rahulshri0703/app100_version:$BUILD_NUMBER"
                sh "docker push rahulshri0703/app100_version:latest"
                //delete the images
                sh " docker rmi rahulshri0703/app100_version:$BUILD_NUMBER"
                sh " docker rmi rahulshri0703/app100_version:latest"
            }
        }
    }
}