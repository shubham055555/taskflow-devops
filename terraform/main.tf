terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }

  required_version = ">= 1.0"
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "taskflow_infra" {
  metadata {
    name = "taskflow-infra"
  }
}

resource "kubernetes_config_map" "taskflow_infra_config" {
  metadata {
    name      = "taskflow-infra-config"
    namespace = kubernetes_namespace.taskflow_infra.metadata[0].name
  }

  data = {
    APP_NAME    = "TaskFlow"
    MANAGED_BY  = "Terraform"
    ENVIRONMENT = "development"
  }
}
