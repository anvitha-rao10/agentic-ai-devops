pipeline {
    agent any

    stages {
        stage('Checkout Code (SSH)') {
            steps {
                git branch: 'main',
<<<<<<< HEAD
                    credentialsId: 'error-ssh-key',
=======
                    credentialsId: 'github-ssh-key',
>>>>>>> 2f26aec61d71451fed29f9c5a6892b214bd18698
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
