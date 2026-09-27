-- 1. Total events by behavior type
SELECT
    is_suspicious,
    COUNT(*) AS total_events
FROM search_interactions
GROUP BY is_suspicious;


-- 2. Click rate by behavior type
SELECT
    is_suspicious,
    AVG(clicked) AS click_rate
FROM search_interactions
GROUP BY is_suspicious;


-- 3. Average dwell time
SELECT
    is_suspicious,
    ROUND(AVG(dwell_time_seconds), 2) AS avg_dwell_time
FROM search_interactions
GROUP BY is_suspicious;

-- 4. Average number of results viewed
SELECT
    is_suspicious,
    ROUND(AVG(num_results_viewed), 2) AS avg_results_viewed
FROM search_interactions
GROUP BY is_suspicious;


-- 5. Query reformulation rate
SELECT
    is_suspicious,
    ROUND(AVG(query_reformulated), 3) AS reformulation_rate
FROM search_interactions
GROUP BY is_suspicious;