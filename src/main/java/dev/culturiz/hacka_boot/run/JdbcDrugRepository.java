//package dev.culturiz.hacka_boot.run;
//
//import org.springframework.jdbc.core.simple.JdbcClient;
//import org.springframework.stereotype.Repository;
//import org.springframework.util.Assert;
//
//import java.util.List;
//import java.util.Optional;
//
//import org.slf4j.Logger;
//import org.slf4j.LoggerFactory;
//import org.springframework.jdbc.core.JdbcTemplate;
//import org.springframework.jdbc.core.RowMapper;
//import org.springframework.jdbc.support.GeneratedKeyHolder;
//import org.springframework.jdbc.support.KeyHolder;
//import org.springframework.stereotype.Repository;
//
//import java.sql.PreparedStatement;
//import java.sql.ResultSet;
//import java.sql.SQLException;
//import java.util.List;
//import java.util.Objects;
//import java.util.Optional;
//
//@Repository
//public class JdbcDrugRepository implements DrugRepository {
//    private static final Logger log = LoggerFactory.getLogger(JdbcDrugRepository.class);
//    private final JdbcTemplate jdbcTemplate;
//
//    public JdbcDrugRepository(JdbcTemplate jdbcTemplate) {
//        this.jdbcTemplate = jdbcTemplate;
//    }
//
//    @Override
//    public List<Drug> findAll() {
//        String sql = "SELECT * FROM drugs";
//        return jdbcTemplate.query(sql, new DrugRowMapper());
//    }
//
//    @Override
//    public Optional<Drug> findById(Integer id) {
//        String sql = "SELECT * FROM drugs WHERE id = ?";
//        try {
//            return Optional.ofNullable(jdbcTemplate.queryForObject(sql, new DrugRowMapper(), id));
//        } catch (Exception e) {
//            log.warn("Drug not found with id {}", id);
//            return Optional.empty();
//        }
//    }
//
//    @Override
//    public void create(Drug drug) {
//        String sql = "INSERT INTO drugs (drug_name, medical_condition, side_effects, generic_name, drug_classes, brand_names, activity, rx_otc, pregnancy_category, csa, alcohol, related_drugs, medical_condition_description, rating, no_of_reviews, drug_link, medical_condition_url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
//
//        KeyHolder keyHolder = new GeneratedKeyHolder();
//
//        jdbcTemplate.update(connection -> {
//            PreparedStatement ps = connection.prepareStatement(sql, new String[]{"id"});
//            ps.setString(1, drug.getDrugName());
//            ps.setString(2, drug.getMedicalCondition());
//            ps.setString(3, drug.getSideEffects());
//            ps.setString(4, drug.getGenericName());
//            ps.setString(5, drug.getDrugClasses());
//            ps.setString(6, drug.getBrandNames());
//            ps.setString(7, drug.getActivity());
//            ps.setString(8, drug.getRxOtc());
//            ps.setString(9, drug.getPregnancyCategory());
//            ps.setString(10, drug.getCsa());
//            ps.setString(11, drug.getAlcohol());
//            ps.setString(12, drug.getRelatedDrugs());
//            ps.setString(13, drug.getMedicalConditionDescription());
//            ps.setObject(14, drug.getRating());
//            ps.setObject(15, drug.getNoOfReviews());
//            ps.setString(16, drug.getDrugLink());
//            ps.setString(17, drug.getMedicalConditionUrl());
//            return ps;
//        }, keyHolder);
//    }
//
//    @Override
//    public void update(Drug drug, Integer id) {
//        String sql = "UPDATE drugs SET drug_name = ?, medical_condition = ?, side_effects = ?, generic_name = ?, drug_classes = ?, brand_names = ?, activity = ?, rx_otc = ?, pregnancy_category = ?, csa = ?, alcohol = ?, related_drugs = ?, medical_condition_description = ?, rating = ?, no_of_reviews = ?, drug_link = ?, medical_condition_url = ? WHERE id = ?";
//
//        int rowsAffected = jdbcTemplate.update(sql,
//                drug.getDrugName(),
//                drug.getMedicalCondition(),
//                drug.getSideEffects(),
//                drug.getGenericName(),
//                drug.getDrugClasses(),
//                drug.getBrandNames(),
//                drug.getActivity(),
//                drug.getRxOtc(),
//                drug.getPregnancyCategory(),
//                drug.getCsa(),
//                drug.getAlcohol(),
//                drug.getRelatedDrugs(),
//                drug.getMedicalConditionDescription(),
//                drug.getRating(),
//                drug.getNoOfReviews(),
//                drug.getDrugLink(),
//                drug.getMedicalConditionUrl(),
//                id);
//
//        if (rowsAffected == 0) {
//            throw new DrugNotFoundException();
//        }
//    }
//
//    @Override
//    public void delete(Integer id) {
//        String sql = "DELETE FROM drugs WHERE id = ?";
//        int rowsAffected = jdbcTemplate.update(sql, id);
//
//        if (rowsAffected == 0) {
//            throw new DrugNotFoundException();
//        }
//    }
//
//    @Override
//    public int count() {
//        return jdbcTemplate.queryForObject("SELECT COUNT(*) FROM drugs", Integer.class);
//    }
//
//    @Override
//    public void saveAll(List<Drug> drugs) {
//        for (Drug drug : drugs) {
//            create(drug);
//        }
//    }
//
//    @Override
//    public List<Drug> findByLocation(String location) {
//        // Assuming this should be findByMedicalCondition instead
//        String sql = "SELECT * FROM drugs WHERE LOWER(medical_condition) LIKE LOWER(?)";
//        return jdbcTemplate.query(sql, new DrugRowMapper(), "%" + location + "%");
//    }
//
//    public List<Drug> findByDrugName(String drugName) {
//        String sql = "SELECT * FROM drugs WHERE LOWER(drug_name) LIKE LOWER(?)";
//        return jdbcTemplate.query(sql, new DrugRowMapper(), "%" + drugName + "%");
//    }
//
//    private static class DrugRowMapper implements RowMapper<Drug> {
//        @Override
//        public Drug mapRow(ResultSet rs, int rowNum) throws SQLException {
//            Drug drug = new Drug();
//            drug.setDrugName(rs.getString("drug_name"));
//            drug.setMedicalCondition(rs.getString("medical_condition"));
//            drug.setSideEffects(rs.getString("side_effects"));
//            drug.setGenericName(rs.getString("generic_name"));
//            drug.setDrugClasses(rs.getString("drug_classes"));
//            drug.setBrandNames(rs.getString("brand_names"));
//            drug.setActivity(rs.getString("activity"));
//            drug.setRxOtc(rs.getString("rx_otc"));
//            drug.setPregnancyCategory(rs.getString("pregnancy_category"));
//            drug.setCsa(rs.getString("csa"));
//            drug.setAlcohol(rs.getString("alcohol"));
//            drug.setRelatedDrugs(rs.getString("related_drugs"));
//            drug.setMedicalConditionDescription(rs.getString("medical_condition_description"));
//            drug.setRating(rs.getObject("rating", Double.class));
//            drug.setNoOfReviews(rs.getObject("no_of_reviews", Integer.class));
//            drug.setDrugLink(rs.getString("drug_link"));
//            drug.setMedicalConditionUrl(rs.getString("medical_condition_url"));
//            return drug;
//        }
//    }
//}
//

package dev.culturiz.hacka_boot.run;

import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public class JdbcDrugRepository implements DrugRepository {

    private final JdbcTemplate jdbcTemplate;
    private final RowMapper<Drug> rowMapper;

    public JdbcDrugRepository(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
        this.rowMapper = (rs, rowNum) -> {
            Drug drug = new Drug();
            drug.setId(rs.getInt("id"));
            drug.setDrugName(rs.getString("drug_name"));
            drug.setMedicalCondition(rs.getString("medical_condition"));
            drug.setSideEffects(rs.getString("side_effects"));
            drug.setGenericName(rs.getString("generic_name"));
            drug.setDrugClasses(rs.getString("drug_classes"));
            drug.setBrandNames(rs.getString("brand_names"));
            drug.setActivity(rs.getString("activity"));
            drug.setRxOtc(rs.getString("rx_otc"));
            drug.setPregnancyCategory(rs.getString("pregnancy_category"));
            drug.setCsa(rs.getString("csa"));
            drug.setAlcohol(rs.getString("alcohol"));
            drug.setRelatedDrugs(rs.getString("related_drugs"));
            drug.setMedicalConditionDescription(rs.getString("medical_condition_description"));
            drug.setRating(rs.getDouble("rating"));
            drug.setNoOfReviews(rs.getInt("no_of_reviews"));
            drug.setDrugLink(rs.getString("drug_link"));
            drug.setMedicalConditionUrl(rs.getString("medical_condition_url"));
            return drug;
        };
        initializeTable();
    }

    private void initializeTable() {
        // First drop the existing table
        jdbcTemplate.execute("DROP TABLE IF EXISTS drugs");

        // Then create a new table with TEXT fields for longer content
        jdbcTemplate.execute("CREATE TABLE drugs ("
                + "id INT AUTO_INCREMENT PRIMARY KEY,"
                + "drug_name VARCHAR(255),"
                + "medical_condition VARCHAR(255),"
                + "side_effects TEXT,"           // Changed from VARCHAR to TEXT
                + "generic_name VARCHAR(255),"
                + "drug_classes VARCHAR(255),"
                + "brand_names TEXT,"            // Changed from VARCHAR to TEXT
                + "activity VARCHAR(50),"
                + "rx_otc VARCHAR(50),"
                + "pregnancy_category VARCHAR(50),"
                + "csa VARCHAR(50),"
                + "alcohol VARCHAR(50),"
                + "related_drugs TEXT,"          // Changed from VARCHAR to TEXT
                + "medical_condition_description TEXT," // Already TEXT
                + "rating DOUBLE,"
                + "no_of_reviews INT,"
                + "drug_link VARCHAR(255),"
                + "medical_condition_url VARCHAR(255)"
                + ")");
    }

    @Override
    public List<Drug> findAll() {
        String sql = "SELECT * FROM drugs";
        return jdbcTemplate.query(sql, rowMapper);
    }

    @Override
    public Optional<Drug> findById(Integer id) {
        try {
            String sql = "SELECT * FROM drugs WHERE id = ?";
            Drug drug = jdbcTemplate.queryForObject(sql, rowMapper, id);
            return Optional.ofNullable(drug);
        } catch (EmptyResultDataAccessException e) {
            return Optional.empty();
        }
    }

    @Override
    public void create(Drug drug) {
        String sql = "INSERT INTO drugs (drug_name, medical_condition, side_effects, generic_name, drug_classes, " +
                "brand_names, activity, rx_otc, pregnancy_category, csa, alcohol, related_drugs, " +
                "medical_condition_description, rating, no_of_reviews, drug_link, medical_condition_url) " +
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

        jdbcTemplate.update(sql,
                drug.getDrugName(),
                drug.getMedicalCondition(),
                drug.getSideEffects(),
                drug.getGenericName(),
                drug.getDrugClasses(),
                drug.getBrandNames(),
                drug.getActivity(),
                drug.getRxOtc(),
                drug.getPregnancyCategory(),
                drug.getCsa(),
                drug.getAlcohol(),
                drug.getRelatedDrugs(),
                drug.getMedicalConditionDescription(),
                drug.getRating(),
                drug.getNoOfReviews(),
                drug.getDrugLink(),
                drug.getMedicalConditionUrl());
    }

    @Override
    public void update(Drug drug, Integer id) {
        String sql = "UPDATE drugs SET drug_name=?, medical_condition=?, side_effects=?, generic_name=?, drug_classes=?, " +
                "brand_names=?, activity=?, rx_otc=?, pregnancy_category=?, csa=?, alcohol=?, related_drugs=?, " +
                "medical_condition_description=?, rating=?, no_of_reviews=?, drug_link=?, medical_condition_url=? " +
                "WHERE id=?";

        jdbcTemplate.update(sql,
                drug.getDrugName(),
                drug.getMedicalCondition(),
                drug.getSideEffects(),
                drug.getGenericName(),
                drug.getDrugClasses(),
                drug.getBrandNames(),
                drug.getActivity(),
                drug.getRxOtc(),
                drug.getPregnancyCategory(),
                drug.getCsa(),
                drug.getAlcohol(),
                drug.getRelatedDrugs(),
                drug.getMedicalConditionDescription(),
                drug.getRating(),
                drug.getNoOfReviews(),
                drug.getDrugLink(),
                drug.getMedicalConditionUrl(),
                id);
    }

    @Override
    public void delete(Integer id) {
        String sql = "DELETE FROM drugs WHERE id = ?";
        jdbcTemplate.update(sql, id);
    }

    @Override
    public int count() {
        try {
            String sql = "SELECT COUNT(*) FROM drugs";
            return jdbcTemplate.queryForObject(sql, Integer.class);
        } catch (Exception e) {
            // Table might not exist yet
            return 0;
        }
    }

    @Override
    public void saveAll(List<Drug> drugs) {
        for (Drug drug : drugs) {
            create(drug);
        }
    }

    @Override
    public List<Drug> findByLocation(String condition) {
        String sql = "SELECT * FROM drugs WHERE medical_condition LIKE ?";
        return jdbcTemplate.query(sql, rowMapper, "%" + condition + "%");
    }

    public List<Drug> findByDrugName(String name) {
        String sql = "SELECT * FROM drugs WHERE drug_name LIKE ?";
        return jdbcTemplate.query(sql, rowMapper, "%" + name + "%");
    }
}