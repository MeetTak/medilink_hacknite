package dev.culturiz.hacka_boot;

import dev.culturiz.hacka_boot.run.Drug;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class HackaBootApplication {

	private static final Logger log = LoggerFactory.getLogger(HackaBootApplication.class);

	public static void main(String[] args) {
		SpringApplication.run(HackaBootApplication.class, args);
	}

	@Bean
	CommandLineRunner runner() {
		return args -> {
			Drug drug = new Drug();
			drug.setDrugName("Adipex-P");
			drug.setMedicalCondition("Weight Loss");
			drug.setSideEffects("hives; difficulty breathing; swelling...");
			drug.setGenericName("phentermine");
			drug.setDrugClasses("Anorexiants");
			drug.setBrandNames("Lomaira");
			drug.setActivity("30%");
			drug.setRxOtc("Rx");
			drug.setPregnancyCategory("X");
			drug.setCsa("4");
			drug.setAlcohol("X");
			drug.setRelatedDrugs("");
			drug.setMedicalConditionDescription("Weight Loss (Obesity/Overweight)...");
			drug.setRating(8.9);
			drug.setNoOfReviews(600);
			drug.setDrugLink("https://www.drugs.com/adipex.html");
			drug.setMedicalConditionUrl("https://www.drugs.com/condition/obesity.html");
			log.info("Drug: {}", drug);
		};
	}
}

