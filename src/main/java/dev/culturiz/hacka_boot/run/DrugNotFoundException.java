package dev.culturiz.hacka_boot.run;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(HttpStatus.NOT_FOUND)
public class DrugNotFoundException extends RuntimeException {
    public DrugNotFoundException() {
        super("Run Not Found");
    }
}
