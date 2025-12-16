pipeline {
    agent any

    stages {
        stage('Checkout Code (SSH)') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-ssh-key',
                    url: 'git@github.com:anvitha-rao10/agentic-ai-devops.git'
            }
        }

        stage('Verify Workspace') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Verify Python (Executor Container)') {
            steps {
                sh '''
                docker exec agentic-ai-devops-env python --version
                '''
            }
        }
    }
}
