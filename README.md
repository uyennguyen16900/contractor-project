![website](https://img.shields.io/website?up_message=online&url=http%3A%2F%2Fcontractor.dev.uyenng.codes%2F)
![image size](https://img.shields.io/docker/image-size/uyennguyen16900/contractor-project)
![circleci build](https://img.shields.io/circleci/build/github/uyennguyen16900/contractor-project)




### Build the image
```bash
docker build -t contractor-image .
```
### Run
```bash
docker run -p 5000:5000 flask-container contractor-image
```
### To see what's running
```bash
docker ps
```
### Docker compose
```bash
docker-compose run
```
### To stop, run
```bash
docker-compose stop
```
