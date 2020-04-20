# MyCalulator
This repo describes a simple calculator developed with python flask(served with default webserver, not to be used in prod) and docker.
Below are the steps for running this application

  - $ git clone https://github.com/ashishsingh2k8/MyCalculator.git/
  - Build the container image locally: $ docker build -t <<<imageName>>> -f Dockerfile . --no-cache 
  - Run the container: $ docker run -d -p 80:80 <<<imageName>>>
 
You can access the swagger UI at http://localhost/swagger/
