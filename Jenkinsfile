
node {
  def package_name = 'wildcard.media'

  catchError {
    stage('Tests') {
      checkout scm
      sh "python3 -m venv ."
      sh "wget -N -q https://dist.plone.org/release/5-latest/requirements.txt"
      sh "./bin/pip install -r requirements.txt"
      sh "./bin/buildout -Nc buildout.cfg"
      sh "./bin/test -s ${package_name}"
    }
  }

  statusSuccess {
    slackSend(color: "good", channel: "#afsoc", message: "${JOB_NAME} - Build #${BUILD_NUMBER} - ${package_name} tests passed")
  }
  statusFailed {
    slackSend(color: "danger", channel: "#afsoc", message: "${JOB_NAME} - Build #${BUILD_NUMBER} - ${package_name} tests failed! Check console output at ${BUILD_URL} to view the results.")
  }
}

def statusSuccess(body) {
  if (currentBuild.currentResult == 'SUCCESS') {
    body()
  }
}

def statusFailed(body) {
  if (currentBuild.currentResult == 'FAILURE') {
    body()
  }
}
