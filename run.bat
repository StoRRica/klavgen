cd test\result
del /q *
cd ../..
docker build -t klavgen-test .
docker create --name dummy klavgen-test
docker cp dummy:/usr/app/src/result ./test
docker rm -f dummy
docker rmi klavgen-test --no-prune