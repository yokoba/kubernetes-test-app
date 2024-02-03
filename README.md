<p style="display: inline">
  <img src="https://img.shields.io/badge/-Kubernetes-326CE5.svg?logo=kubernetes&style=plastic">
  <img src="https://img.shields.io/badge/-Flask-000000.svg?logo=flask&style=plastic">
  <img src="https://img.shields.io/badge/-Docker-1488C6.svg?logo=docker&style=plastic">
</p>

# Project Overview

Manifest file for Kubernetes and application program created for studying Kubernetes operation.

## Environment

The project should work in an environment where Kubernetes is operational.

- Ubuntu 22.04.3 LTS (Jammy Jellyfish)
- minikube version: v1.32.0

# Installation Steps

To run the project, install Minikube.
For detailed instructions, refer to the following link.

- Kubernetes道場 2日目 - Kubernetesのローカル環境について  
  [https://cstoku.dev/posts/2018/k8sdojo-02/](https://cstoku.dev/posts/2018/k8sdojo-02/)

## Usage

You can test the operation using the files under the `kuber_manifest` directory.

### Execution

```
$ minikube start --cpus 4 --memory 4096
$ cd kuber_manifest
$ kubectl apply -f deployment.yaml
$ kubectl apply -f service.yaml
$ kubectl apply -f test.yaml
```

### Operation check

```
$ kubectl get all
NAME                             READY   STATUS    RESTARTS   AGE
pod/food-menu-76656d7d46-ct2vt   4/4     Running   0          5m24s
pod/food-menu-76656d7d46-zvmws   4/4     Running   0          5m24s
pod/food-menu-test               2/2     Running   0          97s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                               AGE
service/food-menu    ClusterIP   10.96.19.193   <none>        1234/TCP,1235/TCP,1236/TCP,8080/TCP   14m
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP                               8d

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/food-menu   2/2     2            2           9m15s

NAME                                   DESIRED   CURRENT   READY   AGE
replicaset.apps/food-menu-76656d7d46   2         2         2       9m15s

$ kubectl logs food-menu-test -c nginx-test
Connecting to food-menu:8080 (10.96.19.193:8080)
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
writing to stdout
-                    100% |********************************|   615  0:00:00 ETA
written to stdout
$
```

### Directory Structure

```
.
├── flask_app
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── kuber_manifest
│   ├── deployment.yaml
│   ├── service.yaml
│   └── test.yaml
└── ReamdMe.txt
```

## Project Structure

- flask_app
  - Files for building the Docker container used in `development.yaml`.
- kuber_manifest
  - Files used for developing with `kubectl`


## License

MIT License

Copyright (c) 2024 yokoba

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
