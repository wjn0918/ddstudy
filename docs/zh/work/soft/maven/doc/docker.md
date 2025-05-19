/usr/share/maven/conf


docker volume create maven_repo -o type=nfs -o device=:$HOME/.m2

-v "$HOME/.m2":/root/.m2


volumes:
  example:
    driver_opts:
      type: "nfs"
      o: bind
      device: ":/docker/example"
