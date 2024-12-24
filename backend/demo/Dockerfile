
FROM openjdk:17-slim

WORKDIR /app
COPY target/demo-0.0.1-SNAPSHOT.jar /app/demo.jar

EXPOSE 8081

CMD ["java", "-jar", "demo.jar"]
