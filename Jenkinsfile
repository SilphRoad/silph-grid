node {
    def app
    def namespace = "camps"
    def deploy = "deploy/silph-grid"
    def imageName = "silph-grid"
    def imageTag = "silph/silph-grid"

    stage('Clone repository') {
        checkout scm
    }

    stage('Build') {
        app = docker.build("${imageTag}:${env.BUILD_NUMBER}")
    }

    stage('Test') {
        app.inside {
            sh 'echo "Tests passed - for now"'
        }
    }

    stage('Publish') {
        if (env.BRANCH_NAME == 'master') {
            docker.withRegistry('https://registry.hub.docker.com', 'silph-gh') {
                app.push()
                app.push("latest")
            }
        } else {
            docker.withRegistry('https://registry.hub.docker.com', 'silph-gh') {
                app.push("${env.BRANCH_NAME}.${env.BUILD_NUMBER}")
            }
        }
    }

    stage('Deploy') {
        if (env.BRANCH_NAME == 'master') {
            withCredentials([file(credentialsId: 'kube-config', variable: 'KUBECONF')]) {
                sh "/snap/kubectl/current/kubectl --kubeconfig=$KUBECONF set image ${deploy} ${imageName}=${imageTag}:${env.BUILD_NUMBER} --namespace ${namespace}"
            }
        } else {
            echo 'I refuse to deploy non-production images 🍔'
        }
    }
}
