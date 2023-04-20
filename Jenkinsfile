pipeline {
    agent  { docker { image 'python:3.10' } }
    stages {
//         stage('Checkout') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/SantosPereira/Flask-RESTful-DIO'
//             }
//         }
        stage('Build') {
            steps {
                script {
                    sh 'ls'
                    docker.build("meu_app_jenkins")
                }
            }
        }
        stage('Run Container') {
            steps {
                script {
                    docker.image("meu_app_jenkins").run("-p 5000:5000 --name meu_app_jenkins_container")
                }
            }
        }
    }
}
