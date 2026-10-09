pipeline {
  agent { label 'python' }
  options {
    timestamps()
    timeout(time: 5, unit: 'MINUTES')
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }
  parameters {
    string(name: 'TARGET', defaultValue: 'world', description: 'Qui saluer')
    booleanParam(name: 'FAIL_ON_PURPOSE', defaultValue: false, description: 'Forcer un échec')
  }
  environment {
    APP_NAME = 'jenkins-lab'
  }
  stages {
    stage('Info') {
      steps {
        sh 'echo "Build ${BUILD_NUMBER} de ${APP_NAME} sur ${NODE_NAME}" && git log -1 --oneline'
      }
    }
    stage('Secrets scan') {
      steps {
        sh 'gitleaks git --no-banner --redact -v .'
      }
    }
    stage('Lint shell') {
      steps {
        sh 'shellcheck scripts/check.sh'
      }
    }
    stage('Lint Python') {
      steps {
        sh 'flake8 scripts/hello.py'
      }
    }
    stage('Test script') {
      steps {
        sh 'chmod +x scripts/check.sh && ./scripts/check.sh "${TARGET}"'
      }
    }
    stage('Run Python') {
      steps {
        sh 'python3 scripts/hello.py "${TARGET}"'
      }
    }
    stage('Outils disponibles') {
      steps {
        sh 'for t in python3 docker git curl; do command -v $t || echo "$t ABSENT"; done'
      }
    }
    stage('Echec volontaire') {
      when { expression { return params.FAIL_ON_PURPOSE } }
      steps { error('Echec demande par le parametre') }
    }
  }
  post {
    always { echo "Statut : ${currentBuild.currentResult}" }
    failure { echo 'Build en echec' }
  }
}
