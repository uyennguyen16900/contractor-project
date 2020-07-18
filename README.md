![website](https://img.shields.io/website?up_message=online&url=http%3A%2F%2Fcontractor.dev.uyenng.codes%2F)
![image size](https://img.shields.io/docker/image-size/uyennguyen16900/contractor-project)
![circleci build](https://img.shields.io/circleci/build/github/uyennguyen16900/contractor-project)



### Clone the repo
```bash
git clone https://github.com/uyennguyen16900/contractor-project.git
```
## Docker
Make sure Docker is running
### Build the image
```bash
docker build -t contractor-image .
```
### Build the container
```bash
docker run -p 5000:5000 flask-container contractor-image
```
### To see what's running
```bash
docker ps
```
### Run
```bash
docker-compose up
```
### To stop, run
```bash
docker-compose down
```
