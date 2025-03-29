package dev.culturiz.hacka_boot.run;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

@Component
public class DrugJsonDataLoader implements CommandLineRunner {

    private static final Logger log = LoggerFactory.getLogger(DrugJsonDataLoader.class);
    private final JdbcDrugRepository drugRepository;
    private final ObjectMapper objectMapper;

    public DrugJsonDataLoader(JdbcDrugRepository drugRepository, ObjectMapper objectMapper) {
        this.drugRepository = drugRepository;
        this.objectMapper = objectMapper;
    }

    @Override
    public void run(String... args) {
        if (drugRepository.count() == 0) {
            log.info("Database is empty. Loading drug data from JSON...");
            try {
                // Load JSON from resources directory
                ClassPathResource resource = new ClassPathResource("data/drugs.json");
                try (InputStream inputStream = resource.getInputStream()) {
                    // Deserialize JSON to List of Drug objects
                    List<Drug> drugs = objectMapper.readValue(inputStream, new TypeReference<List<Drug>>() {});
                    log.info("Found {} drugs in JSON file", drugs.size());

                    // Save all drugs to database
                    drugRepository.saveAll(drugs);
                    log.info("Successfully loaded {} drugs into the database", drugs.size());
                }
            } catch (IOException e) {
                log.error("Failed to load drugs from JSON: {}", e.getMessage(), e);
            }
        } else {
            log.info("Database already contains data. Skipping JSON import.");
        }
    }
}
