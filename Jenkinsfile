pipeline {
  agent any

  environment {
    SOURCE = "jenkins"
  }

  stages {

    stage('Checkout Code (SSH)') {
      steps {
        script {
          try {
            git branch: 'main',
                credentialsId: 'error-ssh-key',
                url: 'git@github.com:anvitha-rao10/agentic-ai-devops.git'
          } catch (err) {
            echo "CHECKOUT_FAILED: ${err}"
            currentBuild.result = 'FAILURE'
          }
        }
      }
    }

    stage('Emit Metadata') {
      steps {
        script {
          def metadata = [
            source: env.SOURCE,
            job_name: env.JOB_NAME,
            build_number: env.BUILD_NUMBER,
            build_url: env.BUILD_URL,
            branch: env.GIT_BRANCH ?: "unknown",
            commit: env.GIT_COMMIT ?: "unknown",
            repo_url: env.GIT_URL ?: "git@github.com:anvitha-rao10/agentic-ai-devops.git",
            stage: "Checkout Code (SSH)",
            error_type: "SSH_AUTH_FAILURE"
          ]

          echo "CI_METADATA: ${groovy.json.JsonOutput.toJson(metadata)}"
        }
      }
    }

    stage('Verify') {
      when {
        expression { currentBuild.result != 'FAILURE' }
      }
      steps {
        sh 'ls -la'
      }
    }
  }
}
