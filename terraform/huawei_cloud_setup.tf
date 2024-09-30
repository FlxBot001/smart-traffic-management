provider "huaweicloud" {
  region = var.region
  access_key = var.access_key
  secret_key = var.secret_key
}

resource "huaweicloud_compute_instance_v2" "example" {
  name            = "example-instance"
  image_id        = var.image_id
  flavor_id       = var.flavor_id
  key_pair        = var.key_pair

  network {
    uuid = var.network_id
  }
}
