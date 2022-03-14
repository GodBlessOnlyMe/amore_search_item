SELECT P.product_no           AS `product_no`,
       P.product_name         AS `product_name`,
       P.product_price        AS `product_price`,
       P.brand_name           AS `brand_name`,
       C.category_depth1_no   AS `category_depth1_no`,
       C.category_depth1_name AS `category_depth1_name`,
       C.category_depth2_no   AS `category_depth2_no`,
       C.category_depth2_name AS `category_depth2_name`
FROM amore.product AS P
LEFT JOIN (
    SELECT L1.category_no                                               AS `category_no`,
           IF(L1.parent_no IS NULL, L1.category_no, L1.parent_no)       AS `category_depth1_no`,
           IF(L1.parent_no IS NULL, L1.category_name, L2.category_name) AS `category_depth1_name`,
           IF(L1.parent_no IS NULL, L1.parent_no, L1.category_no)       AS `category_depth2_no`,
           IF(L1.parent_no IS NULL, L1.parent_no, L1.category_name)     AS `category_depth2_name`
    FROM amore.category AS L1
    LEFT JOIN amore.category AS L2
    ON L2.category_no = L1.parent_no
) AS C
    ON P.category_no = C.category_no