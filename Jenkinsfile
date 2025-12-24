pipeline {
    agent any

    stages {
        stage('Checkout Code (SSH)') {
            steps {
                git branch: 'main',
                  credentialsId: 'error-ssh-key',
                    url: 'git@github.com:anvitha-rao10/agentic-ai-devops.git'
            }
        }

        stage('Verify') {
            steps {
                sh 'ls -la'
            }
        }
    }
}
