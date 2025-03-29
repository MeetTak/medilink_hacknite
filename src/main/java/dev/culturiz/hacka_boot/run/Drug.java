//package dev.culturiz.hacka_boot.run;
//
//public class Drug {
//
//    private Integer id;
//    private String drugName;
//    private String medicalCondition;
//    private String sideEffects;
//    private String genericName;
//    private String drugClasses;
//    private String brandNames;
//    private String activity;
//    private String rxOtc;
//    private String pregnancyCategory;
//    private String csa;
//    private String alcohol;
//    private String relatedDrugs;
//    private String medicalConditionDescription;
//    private Double rating;
//    private Integer noOfReviews;
//    private String drugLink;
//    private String medicalConditionUrl;
//
//    // Default constructor
//    public Drug() {
//    }
//
//    // Getters and setters
//    public Integer getId() {
//        return id;
//    }
//
//    public void setId(Integer id) {
//        this.id = id;
//    }
//
//    public String getDrugName() {
//        return drugName;
//    }
//
//    public void setDrugName(String drugName) {
//        this.drugName = drugName;
//    }
//
//    public String getMedicalCondition() {
//        return medicalCondition;
//    }
//
//    public void setMedicalCondition(String medicalCondition) {
//        this.medicalCondition = medicalCondition;
//    }
//
//    public String getSideEffects() {
//        return sideEffects;
//    }
//
//    public void setSideEffects(String sideEffects) {
//        this.sideEffects = sideEffects;
//    }
//
//    public String getGenericName() {
//        return genericName;
//    }
//
//    public void setGenericName(String genericName) {
//        this.genericName = genericName;
//    }
//
//    public String getDrugClasses() {
//        return drugClasses;
//    }
//
//    public void setDrugClasses(String drugClasses) {
//        this.drugClasses = drugClasses;
//    }
//
//    public String getBrandNames() {
//        return brandNames;
//    }
//
//    public void setBrandNames(String brandNames) {
//        this.brandNames = brandNames;
//    }
//
//    public String getActivity() {
//        return activity;
//    }
//
//    public void setActivity(String activity) {
//        this.activity = activity;
//    }
//
//    public String getRxOtc() {
//        return rxOtc;
//    }
//
//    public void setRxOtc(String rxOtc) {
//        this.rxOtc = rxOtc;
//    }
//
//    public String getPregnancyCategory() {
//        return pregnancyCategory;
//    }
//
//    public void setPregnancyCategory(String pregnancyCategory) {
//        this.pregnancyCategory = pregnancyCategory;
//    }
//
//    public String getCsa() {
//        return csa;
//    }
//
//    public void setCsa(String csa) {
//        this.csa = csa;
//    }
//
//    public String getAlcohol() {
//        return alcohol;
//    }
//
//    public void setAlcohol(String alcohol) {
//        this.alcohol = alcohol;
//    }
//
//    public String getRelatedDrugs() {
//        return relatedDrugs;
//    }
//
//    public void setRelatedDrugs(String relatedDrugs) {
//        this.relatedDrugs = relatedDrugs;
//    }
//
//    public String getMedicalConditionDescription() {
//        return medicalConditionDescription;
//    }
//
//    public void setMedicalConditionDescription(String medicalConditionDescription) {
//        this.medicalConditionDescription = medicalConditionDescription;
//    }
//
//    public Double getRating() {
//        return rating;
//    }
//
//    public void setRating(Double rating) {
//        this.rating = rating;
//    }
//
//    public Integer getNoOfReviews() {
//        return noOfReviews;
//    }
//
//    public void setNoOfReviews(Integer noOfReviews) {
//        this.noOfReviews = noOfReviews;
//    }
//
//    public String getDrugLink() {
//        return drugLink;
//    }
//
//    public void setDrugLink(String drugLink) {
//        this.drugLink = drugLink;
//    }
//
//    public String getMedicalConditionUrl() {
//        return medicalConditionUrl;
//    }
//
//    public void setMedicalConditionUrl(String medicalConditionUrl) {
//        this.medicalConditionUrl = medicalConditionUrl;
//    }
//}
//

package dev.culturiz.hacka_boot.run;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Drug {
    private Integer id;

    @JsonProperty("drug_name")
    private String drugName;

    @JsonProperty("medical_condition")
    private String medicalCondition;

    @JsonProperty("side_effects")
    private String sideEffects;

    @JsonProperty("generic_name")
    private String genericName;

    @JsonProperty("drug_classes")
    private String drugClasses;

    @JsonProperty("brand_names")
    private String brandNames;

    @JsonProperty("activity")
    private String activity;

    @JsonProperty("rx_otc")
    private String rxOtc;

    @JsonProperty("pregnancy_category")
    private String pregnancyCategory;

    @JsonProperty("csa")
    private String csa;

    @JsonProperty("alcohol")
    private String alcohol;

    @JsonProperty("related_drugs")
    private String relatedDrugs;

    @JsonProperty("medical_condition_description")
    private String medicalConditionDescription;

    @JsonProperty("rating")
    private Double rating;

    @JsonProperty("no_of_reviews")
    private Integer noOfReviews;

    @JsonProperty("drug_link")
    private String drugLink;

    @JsonProperty("medical_condition_url")
    private String medicalConditionUrl;

    // Default constructor for JSON deserialization
    public Drug() {}

    // Getters and setters
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getDrugName() {
        return drugName;
    }

    public void setDrugName(String drugName) {
        this.drugName = drugName;
    }

    public String getMedicalCondition() {
        return medicalCondition;
    }

    public void setMedicalCondition(String medicalCondition) {
        this.medicalCondition = medicalCondition;
    }

    public String getSideEffects() {
        return sideEffects;
    }

    public void setSideEffects(String sideEffects) {
        this.sideEffects = sideEffects;
    }

    public String getGenericName() {
        return genericName;
    }

    public void setGenericName(String genericName) {
        this.genericName = genericName;
    }

    public String getDrugClasses() {
        return drugClasses;
    }

    public void setDrugClasses(String drugClasses) {
        this.drugClasses = drugClasses;
    }

    public String getBrandNames() {
        return brandNames;
    }

    public void setBrandNames(String brandNames) {
        this.brandNames = brandNames;
    }

    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }

    public String getRxOtc() {
        return rxOtc;
    }

    public void setRxOtc(String rxOtc) {
        this.rxOtc = rxOtc;
    }

    public String getPregnancyCategory() {
        return pregnancyCategory;
    }

    public void setPregnancyCategory(String pregnancyCategory) {
        this.pregnancyCategory = pregnancyCategory;
    }

    public String getCsa() {
        return csa;
    }

    public void setCsa(String csa) {
        this.csa = csa;
    }

    public String getAlcohol() {
        return alcohol;
    }

    public void setAlcohol(String alcohol) {
        this.alcohol = alcohol;
    }

    public String getRelatedDrugs() {
        return relatedDrugs;
    }

    public void setRelatedDrugs(String relatedDrugs) {
        this.relatedDrugs = relatedDrugs;
    }

    public String getMedicalConditionDescription() {
        return medicalConditionDescription;
    }

    public void setMedicalConditionDescription(String medicalConditionDescription) {
        this.medicalConditionDescription = medicalConditionDescription;
    }

    public Double getRating() {
        return rating;
    }

    public void setRating(Double rating) {
        this.rating = rating;
    }

    public Integer getNoOfReviews() {
        return noOfReviews;
    }

    public void setNoOfReviews(Integer noOfReviews) {
        this.noOfReviews = noOfReviews;
    }

    public String getDrugLink() {
        return drugLink;
    }

    public void setDrugLink(String drugLink) {
        this.drugLink = drugLink;
    }

    public String getMedicalConditionUrl() {
        return medicalConditionUrl;
    }

    public void setMedicalConditionUrl(String medicalConditionUrl) {
        this.medicalConditionUrl = medicalConditionUrl;
    }
}