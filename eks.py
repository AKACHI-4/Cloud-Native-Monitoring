from kubernetes import client, config

# load k8s configuration
config.load_kube_config()

# create a k8s api client
api_client = client.ApiClient()

# define the deployment
deployment = client.V1Deployment(
  metadata=client.V1ObjectMeta(name="cloud-native-monitoring-app"),
  spec=client.V1DeploymentSpec(
    replicas=1,
    selector=client.V1LabelSelector(
      match_labels={"app": "cloud-native-monitoring-app"}
    ),
    template=client.V1PodTemplateSpec(
      metadata=client.V1ObjectMeta(
        labels={"app": "cloud-native-monitoring-app"}
      ),
      spec=client.V1PodSpec(
        containers=[
          client.V1Container(
            name="cloud-native-monitoring-container",
            image="316878774218.dkr.ecr.us-east-1.amazonaws.com/cloud-native-monitoring",
            ports=[client.V1ContainerPort(container_port=5000)]
          )
        ]
      )
    )
  )
)

# create the deployment
api_instance=client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
  namespace="default",
  body=deployment
)

# define the service
service=client.V1Service(
  metadata=client.V1ObjectMeta(name="cloud-native-monitoring-service"),
  spec=client.V1ServiceSpec(
    selector={"app": "cloud-native-monitoring-app"},
    ports=[client.V1ServicePort(port=5000)]
  )
)

# create the service
api_instance=client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
  namespace="default",
  body=service
)
