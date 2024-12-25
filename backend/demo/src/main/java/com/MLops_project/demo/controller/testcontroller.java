package com.MLops_project.demo.controller;

import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;
import org.springframework.http.HttpHeaders;
import org.springframework.stereotype.Controller;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Controller
public class testcontroller {

    @GetMapping("/")
    public String home(){
        return "index";
    }
    private static final Logger logger = LoggerFactory.getLogger(testcontroller.class);
    @Autowired
    private WebClient.Builder webClientBuilder;
    @CrossOrigin(origins = "http://localhost:8080")
    @PostMapping("/predict")
    public Mono<ResponseEntity<String>> predict(@RequestBody String data) {
        String pythonServiceUrl = "http://app:5011/predict";
        logger.info("Received data for prediction: {}", data);
        return webClientBuilder.build()
                .post()
                .uri(pythonServiceUrl)
                .bodyValue(data) 
                .header(HttpHeaders.CONTENT_TYPE, "application/json")
                .retrieve()
                .toEntity(String.class) 
                .onErrorResume(e -> Mono.just(ResponseEntity.internalServerError()
                        .body("Error communicating with Python service: " + e.getMessage())));
    }
}


